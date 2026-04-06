'''

# Exercício Avançado — Triagem de equipamentos devolvidos em uma central de assistência

Uma empresa recebe equipamentos devolvidos de várias filiais. Os registros chegam misturados, com dados repetidos, campos incompletos e classificações inconsistentes.
Você precisa criar um programa em Python que faça a triagem dos itens e decida o destino de cada um.

Use apenas os conteúdos das seções:

* tipos de dados
* estruturas lógicas
* loops
* coleções

---

## Cenário

A central vai analisar vários equipamentos devolvidos.
Cada item possui:

* `id_item` → string
* `categoria` → string
* `dias_devolucao` → número inteiro
* `possui_nota` → boolean
* `lacrado` → boolean
* `status` → string

---

## Coleções obrigatórias no exercício

Seu programa deve usar:

* **lista** para armazenar os itens recebidos
* **dicionário** para registrar o resultado de cada item
* **tupla** para guardar os status permitidos
* **conjunto (set)** para guardar categorias válidas e evitar repetição lógica

---

## Regras do caso

### 1) Cadastro dos itens

O programa deve pedir quantos itens serão analisados.

Depois, para cada item, deve receber os dados acima.

Se `id_item` já tiver sido usado antes, o item deve ser tratado como **duplicado**.

---

### 2) Categorias válidas

As categorias válidas são:

* `"CELULAR"`
* `"NOTEBOOK"`
* `"TABLET"`
* `"ACESSORIO"`

Se a categoria digitada não estiver entre as válidas, o item deve ser colocado como:

* `"Revisão manual necessária"`

---

### 3) Status permitidos

Os status válidos são exatamente estes, guardados em uma **tupla**:

* `"NOVO"`
* `"USADO"`
* `"DANIFICADO"`
* `"INCOMPLETO"`

Regras:

* se status for `"DANIFICADO"`, o item vai para bloqueio
* se status for `"INCOMPLETO"`, o item vai para revisão manual
* se status for `"NOVO"` ou `"USADO"`, o sistema pode continuar a análise

---

### 4) Regra de devolução

* Se `dias_devolucao` for menor que 0, o item é inválido
* Se `dias_devolucao` for maior que 30 e a categoria não for `"CELULAR"`, o caso vira ambíguo
* Se `dias_devolucao` for até 30, a análise segue normalmente

---

### 5) Regra fiscal e lacre

* Se `possui_nota == False`, o item deve ser bloqueado
* Se `lacrado == False`, o item deve ir para revisão manual
* Se os dois forem verdadeiros, segue para decisão final

---

### 6) Regra de prioridade

A central quer tratar primeiro itens de maior risco.

Considere esta ordem de prioridade:

1. `"DANIFICADO"`
2. ausência de nota
3. lacre rompido
4. categoria inválida
5. item duplicado
6. revisão manual
7. acesso liberado

Você deve refletir essa prioridade na lógica do programa.

---

## Saídas possíveis

Cada item deve receber **uma decisão final**:

* `"Acesso permitido"`
* `"Acesso negado"`
* `"Bloqueio por falha de validação"`
* `"Revisão manual necessária"`

---

## O que o programa precisa fazer

1. Ler a quantidade de itens.
2. Ler os dados de cada item.
3. Guardar os `id_item` já vistos em uma estrutura apropriada.
4. Validar categoria, status, lacre, nota e dias de devolução.
5. Classificar cada item com apenas uma decisão final.
6. No fim, mostrar um resumo com:

   * total de itens analisados
   * quantos foram permitidos
   * quantos foram negados
   * quantos foram bloqueados
   * quantos foram para revisão manual

---

## Regras adicionais de lógica

* Se o mesmo `id_item` aparecer mais de uma vez, a segunda ocorrência deve ser marcada como duplicada.
* Se houver conflito entre regras, siga a prioridade definida acima.
* Se tudo estiver válido, o item pode ser permitido.

---

## Restrições

* Não usar funções
* Não usar arquivos
* Não usar `try/except`
* Não usar bibliotecas externas
* Não usar coisas fora do que você já estudou
* Use `if`, `elif`, `else`
* Use `AND`, `OR`, `NOT`
* Use `for`, `while`, `range()` e `break`
* Use listas, dicionários, tuplas e conjuntos

---

## O que eu quero na sua resposta depois de resolver

### Parte 1 — Código

Seu programa completo.

### Parte 2 — Justificativa

Explique a ordem das validações.

### Parte 3 — Riscos

Aponte pelo menos 2 problemas lógicos do seu algoritmo.

### Parte 4 — Alternativa

Mostre outra forma de montar a solução.

---

## Dica de estrutura

Esse exercício fica melhor se você pensar assim:

* um conjunto para controlar duplicados
* uma lista para os itens
* um dicionário para o resultado de cada item
* uma tupla para os status válidos
* um fluxo de decisão por prioridade

'''
itens_permitidos = []
itens_negados = []
itens_bloqueados = []
itens_revisao_manual = []
total_itens = 0
id_duplicado = set()
id_visto = set()
total_duplicados = 0

categorias_validas = ("CELULAR", "NOTEBOOK", "TABLET", "ACESSORIO")
status_permitidos = ("NOVO", "USADO", "DANIFICADO", "INCOMPLETO")

qtd_items = int(input('Quantos items serao analisados? '))

for i in range(qtd_items):
    total_itens += 1

    itens = {}
    id_item = int(input('\ndigite o id do produto? '))
    if id_item in id_visto:
        total_duplicados += 1
        id_duplicado.add(id_item)
        print('id ja existente')
        continue

    id_visto.add(id_item)
    itens.update({'id_item': id_item})
    
    categoria = input(f'Qual a categoria do produto? {categorias_validas}: ').upper().strip()
    if categoria not in categorias_validas:
        print('\nBloqueio por falha de validação') 
        itens_bloqueados.append({'id_item': id_item, 'categoria': 'invalida', 'classificacao': 'Bloqueio por falha de validação'})
        continue
    else:
        itens.update({'categoria': categoria})  

    dias_devolucao = 0
    while True:
        dias_devolucao = int(input('Quantos dias de devolucao? '))
        if dias_devolucao < 0:
            print('\nitem invalido. Tente novamente: \n')

        else:
            break

    if dias_devolucao > 30 and categoria != "CELULAR":
        print('\nRevisão manual necessária')
        itens_revisao_manual.append({'id_item': id_item, 'dias_devolucao': dias_devolucao, 'classificao': 'Revisão manual necessária'})
        continue

    else:
        itens.update({'dias_devolucao': dias_devolucao})
      
    possui_nota = False
    esta_lacrado = False

    while True:
        nota = input('Possui nota fiscal? (s/n): ').lower().strip()
        if nota == 's' or nota == 'n':
            possui_nota = nota == 's'
            break
        else:
            print('\nentrada invalida. Tente novamente: \n')

    if not possui_nota:
        print('\nAcesso negado')
        itens_negados.append({'id_item': id_item, 'possui_nota': possui_nota, 'classificacao': 'Acesso negado'})
        continue
    else:
        itens.update({'possui_nota': possui_nota})

    while True:
        lacrado = input('O item esta lacrado? (s/n): ').lower().strip()
        if lacrado == 's' or lacrado == 'n':
            esta_lacrado = lacrado == 's'
            break
        else:
            print('\nEntrada invalida. Tente novamente\n')

    if not esta_lacrado:
        print('\nRevisão manual necessária')
        itens_revisao_manual.append({'id_item': id_item, 'esta_lacrado': esta_lacrado, 'classificacao': 'Revisão manual necessária'})
        continue

    else:
        itens.update({'esta_lacrado': esta_lacrado})

    status = ''
    while True:
        status = input(f'Qual o status do item? {status_permitidos}: ').upper().strip()
        if status not in status_permitidos:
            print('\nStatus nao identificado. Tente novamente: \n')
        else:
            break
    
    if status == "DANIFICADO":
        print('\nBloqueio por falha de validação')
        itens_bloqueados.append({'id_item': id_item, 'status': status, 'classificacao': 'Bloqueio por falha de validação'})
        continue

    elif status == "INCOMPLETO":
        print('\nRevisão manual necessária')
        itens_revisao_manual.append({'id_item': id_item, 'status': status, 'classificacao': 'Revisão manual necessária'})
        continue

    else:
        itens.update({'status': status})

    itens_permitidos.append(itens)

print('\n========= RESUMO FINAL =========')

print(f'\nTotal de itens analisados: {total_itens}')
print(f'\nQuantos foram permitidos: {len(itens_permitidos)}\n')
for itens in itens_permitidos:
    print(itens)
print(f'\nquantos foram negados: {len(itens_negados)}\n')
for itens in itens_negados:
    print(itens)
print(f'\nQuantos foram bloqueados: {len(itens_bloqueados)}\n')
for itens in itens_bloqueados:
    print(itens)
print(f'\nquantos foram para revisao manual: {len(itens_revisao_manual)}\n')
for itens in itens_revisao_manual:
    print(itens)
print(f'\nQuantos foram duplicados: {total_duplicados}\n')
print(id_duplicado)

