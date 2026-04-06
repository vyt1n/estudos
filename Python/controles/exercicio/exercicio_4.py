'''
Uma empresa de logística recebe lotes de materiais todos os dias.
O problema é que parte dos registros chega com erro humano, campos vazios, classificações 
contraditórias e confirmações incompletas.

Você deve criar um programa em Python para decidir o destino de um lote.

---

## Cenário

O sistema vai receber informações de um lote com destino a uma central de separação.

As entradas serão:

* `peso_kg` → número inteiro
* `categoria` → string
* `possui_etiqueta` → boolean
* `aprovado_fiscal` → boolean
* `status_recebimento` → string
* `tentativa_confirmacao` → string
* `tentativas_revisao` → número inteiro

---

## Regras do caso

### 1) Regra de entrada mínima

O lote só pode continuar no fluxo se:

* `possui_etiqueta == True`
* e `aprovado_fiscal == True`

Se qualquer uma dessas condições falhar, o lote deve ser bloqueado imediatamente.

---

### 2) Categoria do lote

As categorias válidas são apenas:

* `"FRAGIL"`
* `"PESADO"`
* `"URGENTE"`
* `"COMUM"`

Se a categoria for inválida, o sistema deve permitir nova tentativa com `while`.

---

### 3) Regra de peso

* Se `peso_kg` for menor ou igual a 0, o lote é inválido.
* Se `peso_kg` for maior que 80 e a categoria não for `"PESADO"`, o caso fica ambíguo.
* Se `peso_kg` estiver entre 1 e 80, a análise pode continuar.

---

### 4) Status de recebimento

O campo `status_recebimento` pode vir com estes valores válidos:

* `"OK"`
* `"PENDENTE"`
* `"RECUSADO"`

Regras:

* Se for `"RECUSADO"`, bloquear imediatamente.
* Se for `"PENDENTE"`, permitir revisão.
* Se for `"OK"`, seguir para a próxima etapa.

---

### 5) Confirmação manual

Antes da decisão final, o sistema deve validar `tentativa_confirmacao` com até **3 tentativas**.

Regras:

* O valor correto é `"CONFIRMAR"`
* Se errar, deve permitir tentar novamente
* Se acertar antes das 3 tentativas, usar `break`
* Se errar 3 vezes, encerrar com bloqueio

---

### 6) Regra de revisão

Se `tentativas_revisao` for maior ou igual a 2, o lote deve ir para revisão manual, mesmo que o resto esteja válido.

---

## Situações ambíguas

Você pode decidir entre:

* `"Acesso negado"`
* `"Revisão manual necessária"`

em casos como:

* peso muito alto com categoria incompatível
* status `PENDENTE` com demais dados corretos
* lote válido, mas com histórico de revisão alto

A escolha precisa ser coerente com a lógica que você montar.

---

## Saídas possíveis

O programa deve terminar com **apenas uma** destas mensagens:

* `"Acesso permitido"`
* `"Acesso negado"`
* `"Bloqueio por falha de validação"`
* `"Revisão manual necessária"`

---

## O que o programa precisa fazer

1. Ler os dados.
2. Validar se o lote pode continuar no fluxo.
3. Usar `while` para corrigir entradas inválidas.
4. Aplicar as regras de peso, categoria e status.
5. Validar a confirmação manual com limite de tentativas.
6. Encerrar com uma única decisão final.

---

## Restrições

* Não usar funções
* Não usar listas
* Não usar dicionários
* Não usar `try/except`
* Não usar recursos fora do que você listou nas seções

---

## O foco aqui

Esse exercício foi desenhado para te forçar a trabalhar com:

* `while` para repetição de validação
* `if / elif / else` para decisões em camadas
* `AND / OR / NOT` para combinar regras
* variáveis booleanas para controlar fluxo
* escopo bem organizado para não bagunçar o programa

'''
etiqueta = ''
fiscal = ''
status_recebimento = ''

while True:
    status_recebimento = input('Qual os status da entrega do lote? ("OK", "PENDENTE" ou "RECUSADO"): ').upper().strip()

    if status_recebimento != "OK" and status_recebimento != "PENDENTE" and status_recebimento != "RECUSADO":
        print('Opcao invalida. Tente novamente')

    else:
        break

if status_recebimento == "RECUSADO":
    print('Bloqueio por falha de validação')

elif status_recebimento == "PENDENTE":
    print('Revisao manual necessaria')

else:
    while True:
        etiqueta = input('O lote Possui etiqueta? (s/n): ').lower().strip()
        fiscal = input('O lote Possui nota fiscal? (s/n): ').lower().strip()

        if etiqueta != 's' and etiqueta != 'n': 
            print('Opcao invalida. Nao existe essa opcao. Tente novamente') 

        elif fiscal != 's' and fiscal != 'n': 
            print('Opcao invalida. Nao existe essa opcao. Tente novamente')

        else:
            break

    possui_etiqueta = etiqueta == 's'
    aprovado_fiscal = fiscal == 's'

    if not possui_etiqueta or not aprovado_fiscal:
        print('Acesso negado')

    else:
        peso_kg = int(input('Qual o peso do lote? '))

        if peso_kg <= 0:
            print('Bloqueio por falha de validação')

        else:
            categoria = ''

            while True:
                categoria = input('Qual é a categoria desse lote ("FRAGIL", "PESADO", "URGENTE" ou "COMUM")? ').upper().strip()

                if categoria != "FRAGIL" and categoria != "PESADO" and categoria != "URGENTE" and categoria != "COMUM":
                    print('Opcao invalida. Tente novamente: ')

                else:
                    break

            if peso_kg > 80 and categoria != "PESADO":
                print('Revisão manual necessária')

            else:


                tentativas_revisao = 0

                for tentativas in range(3):
                    confirmar = input('Confirmar revisao? ("CONFIRMAR"): ').upper().strip()
                    tentativas_revisao += 1

                    if confirmar == "CONFIRMAR":
                        break

                    else:
                        if tentativas < 2:
                            print('confirmacao incorreta. Tente novamente: ')
                        else:
                            print('Tentativas de confirmacao excedidas')
                
                if tentativas_revisao == 3:
                    print('Bloqueio por falha de validação')

                elif tentativas_revisao > 1:
                    print('Revisao manual necessaria')

                else:
                    print('Acesso permitido')