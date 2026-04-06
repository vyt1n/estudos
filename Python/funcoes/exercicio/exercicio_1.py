'''
### Título do Problema

**Triagem de Carrinho de E-commerce para Fechamento de Pedido**

### Descrição do Cenário

Uma loja online recebe uma lista de itens que um cliente quer comprar antes de finalizar o pedido.
Antes de confirmar a compra, o sistema precisa:

* evitar produtos repetidos;
* rejeitar itens inválidos;
* calcular o valor total corretamente;
* aplicar desconto conforme regras do negócio;
* gerar um resumo final do carrinho.

Isso acontece na vida real para evitar erro de cobrança, duplicidade de itens e falhas no checkout.

### Requisitos Funcionais

Seu programa deve:

1. Ler a quantidade de itens que o cliente deseja cadastrar.
2. Ler, para cada item:

   * nome do produto (`string`)
   * categoria (`string`)
   * preço unitário (`numérico`)
   * quantidade (`numérico`)
   * prioridade do item (`boolean`, `True` ou `False`)

3. Ignorar itens com:

   * preço menor ou igual a zero;
   * quantidade menor ou igual a zero;
   * categoria fora da lista permitida;
   * nome de produto repetido.

4. Armazenar os itens válidos em uma **lista de dicionários**.
5. Usar um **set** para controlar quais produtos já foram inseridos.
6. Usar uma **tupla** com as categorias permitidas.
7. Calcular o subtotal dos itens válidos.
8. Aplicar desconto seguindo estas regras:

   * se o subtotal for maior ou igual a 500 **e** não houver item prioritário: desconto de 10%;
   * senão, se o subtotal for maior ou igual a 200 **ou** houver item prioritário: desconto de 5%;
   * caso contrário: sem desconto.
9. Exibir:

   * quantidade de itens válidos;
   * quantidade de itens ignorados;
   * subtotal;
   * desconto;
   * total final.

### Restrições Técnicas

Você deve usar:

* `if`, `elif`, `else`
* operadores `and`, `or`, `not`
* `for` com `range()`
* pelo menos um `while`
* pelo menos um `break`
* `def` para criar funções
* `return`
* pelo menos uma função com parâmetro padrão
* pelo menos uma função usando `*args`
* pelo menos uma função usando `**kwargs`
* listas, dicionários, tuplas e conjuntos

Você não pode usar bibliotecas externas.

### Exemplo de Entrada/Saída Esperado

**Entrada**

4
Mouse periferico 80 2 False
Teclado periferico 120 1 True
Mouse periferico 80 1 False
Cadeira escritorio 300 1 False
```

**Saída**

Resumo do carrinho
Itens válidos: 3
Itens ignorados: 1
Subtotal: 580.00
Desconto: 29.00
Total final: 551.00
```

'''

def nome_produto(mensagem):
    while True:
        nome = input(mensagem).strip().title()
        if nome == '':
            print('Entrada invalida. Tente novamente: ')
        else:
            return nome
  
def categoria_produto(mensagem, categoria_valida):
    while True:
        categoria = input(mensagem).strip().upper()
        if categoria not in categoria_valida:
            print('categoria invalida. Tente novamente: ')
        else:
            return categoria
        
def quantidade_valida(mensagem):
    while True:
        quantidade = int(input(mensagem))
        if quantidade <= 0:
            print('quantidade invalida. Tente novamente: ')
        else:
            return quantidade  

def validacao_prioridade(mensagem):
    while True:
        prioridade_item = input(mensagem).strip().lower()
        if prioridade_item not in ('s', 'n'):
            print('opcao invalida. Tente novamente: ')
        else:
            prioridade_item = (prioridade_item == 's')
            break

    return prioridade_item

def soma(preco, quantidade):
    return preco * quantidade

def desconto(subtotal, prioridade):
    if subtotal >= 500 and not prioridade:
        return subtotal * 0.1
    elif subtotal >= 200 or prioridade:
        return subtotal * 0.05
    else:
        return 0
    

cadastros = []

qtd_itens = int(input('Quantos itens deseja cadastrar: '))

for i in range(qtd_itens):
    cadastro = {}

    print(f'\nItem {i + 1}: \n')

    nome = nome_produto('Nome do produto: ')
    cadastro.update({'nome': nome})

    categoria_valida = ("PERIFERICOS", "MONITORES", "PLACA DE VIDEO", "PLACA MAE", "ESCRITORIO")
    categoria = categoria_produto(f'qual a categoria do produto {categoria_valida}: ', categoria_valida)
    cadastro.update({'categoria': categoria}) 

    preco = quantidade_valida('preco unitario: ')
    cadastro.update({'preco unitario': preco})

    quantidade = quantidade_valida('quantidade: ')
    cadastro.update({'quantidade': quantidade})

    prioridade = validacao_prioridade('prioridade (s/n): ')
    cadastro.update({'prioridade': prioridade})

    cadastros.append(cadastro)

itens_validos = 0
itens_ignorados = 0
subtotal = 0
tem_prioridade = False

produto_duplicado = set()

for item in cadastros:
    if item['nome'] in produto_duplicado:
        itens_ignorados += 1
        continue
    
    produto_duplicado.add(item['nome'])
    itens_validos += 1

    subtotal += soma(item['preco unitario'], item['quantidade'])  

    if item['prioridade']:
        tem_prioridade = True

descontos = desconto(subtotal, tem_prioridade)
total_final = subtotal - descontos

print('\n========== RESUMO DO CARRINHO ==========\n')

print(f'Itens validos: {itens_validos}')
print(f'Itens ignorados: {itens_ignorados}')
print(f'Subtotal: {subtotal}')
print(f'Desconto: {descontos}')
print(f'Total final: {total_final}')