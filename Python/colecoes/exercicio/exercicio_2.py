'''
## **Validação de Cadastros de Pacientes para Triagem Inicial (Saúde)**

### **Descrição do Cenário**

Em uma clínica, nem todo cadastro pode seguir para atendimento automático. Antes disso, o sistema precisa validar dados mínimos para evitar erros como idade inválida, 
tipo de plano inexistente ou cadastro duplicado.

Você vai criar um programa que analisa vários pacientes e decide se cada cadastro está **válido** ou **inválido**.

---

### **Requisitos Funcionais**

O programa deve:

1. Perguntar quantos pacientes serão analisados.

2. Para cada paciente, receber os seguintes dados:

   * `id_paciente` → string
   * `nome` → string
   * `idade` → inteiro
   * `tem_plano` → booleano (`True` ou `False`)
   * `tipo_plano` → string

3. Validar cada cadastro com as regras abaixo:

   * `id_paciente` não pode se repetir
   * `idade` deve ser maior ou igual a 0
   * `nome` não pode ser vazio
   * Se `tem_plano` for `True`, o `tipo_plano` deve ser um dos seguintes:

     * `"basico"`
     * `"intermediario"`
     * `"premium"`
   * Se `tem_plano` for `False`, o `tipo_plano` deve obrigatoriamente ser `"nenhum"`

4. Para cada paciente, armazenar o resultado em um dicionário no formato:

   ```python
   {
       id_paciente: (status, motivo)
   }
   ```

   Onde:

   * `status` pode ser `"valido"` ou `"invalido"`
   * `motivo` deve explicar o primeiro erro encontrado, ou `"ok"` se estiver correto

5. Ao final, mostrar:

   * todos os resultados
   * total de cadastros válidos
   * total de cadastros inválidos

---

### **Restrições Técnicas**

Você **deve usar**:

* `list` para guardar os pacientes recebidos
* `dict` para guardar os resultados
* `tuple` para representar `(status, motivo)`
* `set` para guardar os tipos de plano permitidos
* `if`, `elif`, `else`
* `and`, `or`, `not`
* `for`
* `while`
* `break` em algum ponto lógico

Você **não pode usar**:

* bibliotecas externas
* estruturas prontas de validação
* funções prontas que resolvam o problema por você

---

### **Exemplo de Entrada**

```python
Quantos pacientes? 3

Paciente 1:
id_paciente: P01
nome: Ana
idade: 25
tem_plano: True
tipo_plano: premium

Paciente 2:
id_paciente: P02
nome: Bruno
idade: -3
tem_plano: False
tipo_plano: nenhum

Paciente 3:
id_paciente: P01
nome: Carla
idade: 40
tem_plano: True
tipo_plano: basico
```

---

### **Exemplo de Saída Esperada**

```python
Resultados:

P01 -> ('valido', 'ok')
P02 -> ('invalido', 'idade invalida')
P01 -> ('invalido', 'id duplicado')

Resumo:
Validos: 1
Invalidos: 2
```

---

### **Desafio adicional opcional**

Se quiser aumentar a dificuldade, faça o programa também:

* contar quantos pacientes têm plano
* contar quantos não têm plano
* parar a execução se encontrar **3 IDs repetidos**

'''
pacientes_recebidos = []
pacientes_validos = []
pacientes_invalidos = []

planos = ("BASICO", "INTERMEDIARIO", "PREMIUM")

id = set()
ids_repetidos = set()

qtd_id_repetidos = 0
qtd_recebidos = 0
qtd_validos = 0
qtd_invalidos = 0

qtd_pacientes = int(input('Quantos pacientes serao analisados: '))

for i in range(qtd_pacientes):
    qtd_recebidos += 1

    print(f'\nPaciente {i + 1}: \n')

    paciente = {}
         
    id_paciente = input('Digite o id do paciente: ').strip()
    paciente.update({'id': id_paciente})   
    
    while True:
        nome = input('Nome do paciente: ').strip().title()
        if nome == '':
            print('Nome vazio. Tente novamente')
        
        else:
            paciente.update({'nome': nome})
            break
        
    idade = int(input('Idade do paciente: '))
    paciente.update({'idade': idade})

    tem_plano = False
    while True:
        plano = input('O paciente tem plano de saude? (s/n): ').lower().strip()
        if plano != 's' and plano != 'n':
            print('Opcao invalida. Tente novamente')
        
        else:
            tem_plano = (plano == 's')   
            paciente.update({'tem plano': tem_plano})
            break

    tipo_plano = ''
    if not tem_plano:
        paciente.update({'tipo do plano': 'Nenhum'})
    else:
        while True:
            tipo_plano = input(F'Qual o tipo do plano? {planos}: ').upper().strip()
            if tipo_plano not in planos:
                print('Opcao invalida. Tente novamente: ')
            else:
                paciente.update({'tipo do plano': tipo_plano})
                break

    pacientes_recebidos.append(paciente)

    if id_paciente in id:       
        ids_repetidos.add(id_paciente)
        pacientes_invalidos.append({id_paciente: ('invalido', 'id duplicado')})
        qtd_invalidos += 1
        qtd_id_repetidos += 1
        continue

    elif idade < 0:
        pacientes_invalidos.append({id_paciente: ('invalido', 'idade invalida')})
        qtd_invalidos += 1
        continue
    
    else:
        id.add(id_paciente)
        pacientes_validos.append({id_paciente: ('valido', 'ok')})
        qtd_validos += 1

print('\n========== RESULTADOS ==========\n')

for i in pacientes_recebidos:
    print(i)
print()
for i in pacientes_validos:
    print(i)
print()
for i in pacientes_invalidos:
    print(i)
print()
print(ids_repetidos)

print('\n========== RESUMO ==========\n')

print(f'Quantidade de pacientes recebidos: {qtd_recebidos}')
print(f'Quantidade de pacientes validos: {qtd_validos}')
print(f'Quantidade de pacientes invalidos: {qtd_invalidos}')
print(f'Quantidade de id repetido: {qtd_id_repetidos}')