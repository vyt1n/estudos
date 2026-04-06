'''
## **Triagem de Pedidos para Separação de Estoque (E-commerce)**

### **Descrição do Cenário**

Uma loja online recebe pedidos o tempo todo. Antes de enviar qualquer pacote para o setor de expedição, o sistema precisa verificar se o pedido realmente pode seguir para separação. Isso evita erro de estoque, pedido duplicado e liberação de compras com dados incoerentes.

Seu programa vai simular essa triagem automática. A ideia é organizar os dados com cuidado e decidir, com lógica clara, quais pedidos são aprovados e quais devem ser recusados.

---

### **Requisitos Funcionais**

O programa deve:

1. Perguntar quantos pedidos serão analisados.

2. Para cada pedido, receber:

   * `id_pedido` → string
   * `cliente` → string
   * `produto` → string
   * `quantidade` → inteiro
   * `estoque_disponivel` → inteiro
   * `pagamento_aprovado` → boolean (`True` ou `False`)
   * `categoria_cliente` → string

3. Validar cada pedido seguindo esta ordem:

   * o `id_pedido` não pode se repetir
   * `quantidade` deve ser maior que 0
   * `estoque_disponivel` deve ser maior ou igual a 0
   * `pagamento_aprovado` deve ser `True`
   * `categoria_cliente` deve ser uma das categorias permitidas:

     * `"comum"`
     * `"premium"`
     * `"vip"`

4. Regra extra de negócio:

   * se o cliente for `"vip"`, o pedido pode seguir mesmo com prioridade maior, mas ainda precisa passar nas validações acima
   * se a quantidade pedida for maior que o estoque disponível, o pedido deve ser recusado com motivo de estoque insuficiente

5. Armazenar o resultado de cada pedido em um dicionário no formato:

   ```python
   {
       id_pedido: (status, motivo)
   }
   ```

   Onde:

   * `status` é `"aprovado"` ou `"reprovado"`
   * `motivo` é o primeiro erro encontrado, ou `"ok"` se estiver tudo certo

6. Ao final, exibir:

   * todos os pedidos analisados
   * o dicionário de resultados
   * a quantidade de pedidos aprovados
   * a quantidade de pedidos reprovados

---

### **Restrições Técnicas**

Você **deve usar**:

* `list` para guardar os pedidos recebidos
* `dict` para guardar os resultados
* `tuple` para guardar os status permitidos
* `set` para guardar as categorias válidas e os IDs já usados
* `if`, `elif`, `else`
* `and`, `or`, `not`
* `for`
* `while`
* `break`

Você **não pode usar** bibliotecas externas, funções prontas de validação ou estruturas que resolvam a lógica por você.

---

### **Exemplo de Entrada / Saída esperada**

#### **Entrada**

```python
Quantos pedidos serão analisados? 3

Pedido 1:
id_pedido: P100
cliente: Ana
produto: Mouse
quantidade: 2
estoque_disponivel: 10
pagamento_aprovado: True
categoria_cliente: premium

Pedido 2:
id_pedido: P101
cliente: Bruno
produto: Teclado
quantidade: 5
estoque_disponivel: 3
pagamento_aprovado: True
categoria_cliente: comum

Pedido 3:
id_pedido: P100
cliente: Carla
produto: Headset
quantidade: 1
estoque_disponivel: 8
pagamento_aprovado: False
categoria_cliente: vip
```

#### **Saída esperada**

```python
Pedidos analisados:
[
  {'id_pedido': 'P100', 'cliente': 'Ana', 'produto': 'Mouse', 'quantidade': 2, 'estoque_disponivel': 10, 'pagamento_aprovado': True, 'categoria_cliente': 'premium'},
  {'id_pedido': 'P101', 'cliente': 'Bruno', 'produto': 'Teclado', 'quantidade': 5, 'estoque_disponivel': 3, 'pagamento_aprovado': True, 'categoria_cliente': 'comum'},
  {'id_pedido': 'P100', 'cliente': 'Carla', 'produto': 'Headset', 'quantidade': 1, 'estoque_disponivel': 8, 'pagamento_aprovado': False, 'categoria_cliente': 'vip'}
]

Resultados:
{
  'P100': ('reprovado', 'id duplicado'),
  'P101': ('reprovado', 'estoque insuficiente')
}

Aprovados: 1
Reprovados: 2
```

---

### **Observação importante para treinar bem**

Antes de codar, pense nesta ordem:

1. onde guardar cada pedido recebido;
2. onde guardar os IDs já usados;
3. em que momento validar;
4. como parar no primeiro erro;
5. como montar a saída final sem bagunçar a lógica.

'''

pedidos_recebidos = []

produtos_disponiveis = {"COMPUTADOR", "NOTEBOOK", "CELULAR", "MOUSE", "TECLADO"}
categorias_validas = {"COMUM", "PREMIUM", "VIP"}

qtd_pedidos = int(input('Quantos pedidos serao analisados? '))

for i in range(qtd_pedidos):
   print(f'\npedido {i + 1}: \n')

   pedidos = {}

   while True:
      id_pedido = input('id do pedido: ').strip()
      if id_pedido == '':
         print('ID invalido. Tente novamente: ')
      else:
         pedidos['id'] = id_pedido
         break

   cliente = input(f'cliente: ').strip().title()
   pedidos['cliente'] = cliente

   while True:
      produto = input(f'Produto {produtos_disponiveis}: ').strip().upper()

      if produto not in produtos_disponiveis:
         print('produto indisponivel. Tente novamente: ')
      else:
         pedidos['produto'] = produto
         break        

   while True:   
      quantidade = int(input('Quantidade do produto: '))
      if quantidade <= 0:
         print('Quantidade invalida. Tente novamente: ')
      else:
         pedidos['quantidade'] = quantidade
         break

   while True:
      estoque = int(input('estoque disponivel: '))
      if estoque < 0:
         print('estoque invalido. Tente novamente: ')
      else:
         pedidos['estoque'] = estoque
         break
 
   while True:     
      entrada_pagamento = input('pagamento aprovado (s/n): ').strip().lower()

      if entrada_pagamento not in ('s', 'n'):
         print('opcao invalida. Tente novamente')
      else:
         pagamento = (entrada_pagamento == 's')
         pedidos['pagamento'] = pagamento
         break

   while True:
      categoria = input(f'Categoria do cliente {categorias_validas}: ').strip().upper()
      if categoria not in categorias_validas:
         print('Categoria invalida. Tente novamente: ')
      else:
         pedidos['categoria'] = categoria
         break

   pedidos_recebidos.append(pedidos)

resultado_pedidos = {}
ids = set()
id_duplicado = set()

qtd_validos = 0
qtd_invalidos = 0

for item in pedidos_recebidos:
   status = "VALIDO"
   motivo = "OK"

   if item['id'] in ids:
      qtd_invalidos += 1
      id_duplicado.add(item['id'])
      status = "INVALIDO"
      motivo = "ID DUPLICADO"
   else:
      ids.add(item['id'])

      if item['quantidade'] > item['estoque']:
         qtd_invalidos += 1
         status = "INVALIDO"
         motivo = "ESTOQUE INDISPONIVEL"

      elif not item['pagamento']:
         qtd_invalidos += 1
         status = "INVALIDO"
         motivo = "PAGAMENTO NAO REALIZADO"
      
      else:
         qtd_validos += 1

   resultado_pedidos[item['id']] = (status, motivo)

print('\n========== PEDIDOS ANALISADOS ==========\n')

for i in pedidos_recebidos:
   print(i)

print('\n========== RESULTADOS ==========\n')

for chave, valor in resultado_pedidos.items():
   print(f'{chave} -> {valor}')

print()
print(f'Pedidos validos: {qtd_validos}\nPedidos invalidos: {qtd_invalidos}')

if id_duplicado:
    print(f'id`s duplicados: {id_duplicado}')
else:
    print("Nenhum ID duplicado encontrado")