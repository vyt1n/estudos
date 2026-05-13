'''
## 🍕 Sistema de Gestão de Pedidos — "FastByte Lanchonete"

Você foi contratado para construir o **backend de um sistema de pedidos** de uma lanchonete. 
O sistema precisa controlar o cardápio, processar pedidos, aplicar regras de negócio e 
gerar relatórios.

---

### 📦 Dados do sistema

Trabalhe com as seguintes estruturas como ponto de partida:

cardapio = {
    "X-Burguer":    {"preco": 18.50, "categoria": "lanche",   "disponivel": True},
    "X-Bacon":      {"preco": 24.00, "categoria": "lanche",   "disponivel": True},
    "Fritas":       {"preco": 10.00, "categoria": "acomp",    "disponivel": True},
    "Refrigerante": {"preco":  7.50, "categoria": "bebida",   "disponivel": True},
    "Suco Natural": {"preco":  9.00, "categoria": "bebida",   "disponivel": False},
    "Sorvete":      {"preco": 12.00, "categoria": "sobremesa","disponivel": False},
}

pedidos_dia = [
    {"cliente": "Ana",    "itens": ["X-Burguer", "Fritas", "Refrigerante"], "pago": True},
    {"cliente": "Bruno",  "itens": ["X-Bacon", "Suco Natural"],             "pago": False},
    {"cliente": "Carla",  "itens": ["Fritas", "Refrigerante"],              "pago": True},
    {"cliente": "Diego",  "itens": ["X-Bacon", "Sorvete", "Refrigerante"],  "pago": False},
    {"cliente": "Elena",  "itens": ["X-Burguer", "X-Bacon", "Fritas"],      "pago": True},
]
```

---

### ✅ Tarefas

Implemente **cada item como uma função separada**.

---

#### 1. `validar_pedido(itens)`
Recebe uma lista de itens de um pedido e retorna uma **tupla** `(valido, motivo)`.

- Um pedido é **inválido** se contiver algum item indisponível **ou** se estiver vazio
- `valido` → `bool`, `motivo` → `str` explicando o resultado
- Use `AND`, `OR`, `NOT` nas validações

---

#### 2. `calcular_total(itens, desconto=0)`
Recebe a lista de itens e um percentual de desconto **opcional** (padrão = 0).

- Retorna o valor total já com desconto aplicado
- Se o total **antes** do desconto passar de R$ 50,00 → aplica automaticamente mais **10% 
  adicional** em cima do desconto já passado
- Itens **indisponíveis** no cardápio devem ser **ignorados** no cálculo (não geram erro)

---

#### 3. `resumo_pedidos(*pedidos, **opcoes)`
Recebe múltiplos dicionários de pedido via `*args` e opções via `**kwargs`.

Opções possíveis:
- `apenas_pagos=True` → filtra somente pedidos pagos
- `categoria="bebida"` → filtra pedidos que contenham ao menos 1 item dessa categoria

Retorna uma **lista** com os nomes dos clientes que passaram nos filtros.

> Use `*args` e `**kwargs` de verdade — a função não sabe quantos pedidos vai receber.

---

#### 4. `gerar_relatorio(pedidos)`
Usando **comprehensions** (obrigatório para cada item abaixo), gere e retorne um dicionário com:

```python
{
  "totais_por_cliente":  # dict comprehension → {nome: total_do_pedido}
  "clientes_devedores":  # list comprehension → [nomes com pago=False]
  "categorias_pedidas":  # set comprehension → categorias únicas de todos os itens pedidos
}
```

---

#### 5. `menu_interativo()`
Um loop `while` que simula o atendimento:

- Exibe os itens **disponíveis** do cardápio com preços
- Pede ao usuário para digitar o nome do item ou `"fim"` para encerrar
- Vai **acumulando** os itens escolhidos em uma lista
- Se o item não existir ou estiver indisponível → avisa e **continua** (não quebra o loop)
- Ao digitar `"fim"` → usa `break`, chama `calcular_total()` e exibe o valor final

---

### 🏁 Desafio final (opcional)

Crie uma função `processar_dia()` que:
1. Percorre `pedidos_dia` com um `for`
2. Valida cada pedido com `validar_pedido()`
3. Se válido → calcula o total com `5%` de desconto para clientes que pagaram
4. Imprime um resumo linha a linha:
```
[VÁLIDO]   Ana     → R$ 32.87  ✔ pago
[INVÁLIDO] Bruno   → item indisponível: Suco Natural
```
'''

cardapio = {
    "X-Burguer":    {"preco": 18.50, "categoria": "lanche",    "disponivel": True},
    "X-Bacon":      {"preco": 24.00, "categoria": "lanche",    "disponivel": True},
    "Fritas":       {"preco": 10.00, "categoria": "acomp",     "disponivel": True},
    "Refrigerante": {"preco":  7.50, "categoria": "bebida",    "disponivel": True},
    "Suco Natural": {"preco":  9.00, "categoria": "bebida",    "disponivel": False},
    "Sorvete":      {"preco": 12.00, "categoria": "sobremesa", "disponivel": False},
}

def validar_pedido(pedido):
    itens = pedido.get('itens')

    if not itens:
        return (False, 'Itens vazios')
    
    for item in itens:
        if item not in cardapio:
            return (False, f'item {item} nao existe')
        
        if not cardapio[item]['disponivel']:
            return (False, f'item {item} indisponivel')
        
    return (True, f'Pedido {itens} disponivel')

def calcular_total(pedido, desconto=0):
    itens = pedido.get('itens')
    
    valor_itens = 0
    for item in itens:
        if item in cardapio:
            if cardapio[item]['disponivel']:
                valor_itens += cardapio[item]['preco']

    valor_desconto = valor_itens * (desconto/100)
    valor_total = valor_itens - valor_desconto

    if valor_itens > 50:
        desconto_adicional = valor_total * (10/100)
        valor_total -= desconto_adicional
        
    
    return f'{valor_total:.2f}'

def resumo_pedidos(*pedidos, **opcoes):

    clientes_aprovados = []
    apenas_pago = opcoes.get('apenas_pago')
    categoria = opcoes.get('categoria')

    for pedido in pedidos:
        if apenas_pago and not pedido['pago']:
            continue
        if categoria:
            tem_categoria = False
            for item in pedido['itens']:
                if cardapio[item]['categoria'] == categoria:
                    tem_categoria = True
            
            if not tem_categoria:
                continue
        
        clientes_aprovados.append(pedido['cliente'])

    return clientes_aprovados

def gerar_relatorio(pedidos):
    totais_pot_clientes = {pedido['cliente']: calcular_total(pedido) for pedido in pedidos}
    clientes_devedores = [pedido['cliente'] for pedido in pedidos if not pedido['pago']]
    categorias_pedidas = {cardapio[item]['categoria'] for pedido in pedidos for item in pedido['itens'] if cardapio[item]['disponivel']}

    return {'total por cliente': totais_pot_clientes,
            'clientes devedores': clientes_devedores, 
            'categorias pedidas': categorias_pedidas}

def menu_interativo():
    nome = input('Nome do cliente: ')
    itens_escolhidos = []

    print('\nCardapio disponivel:')
    for nome_item, info in cardapio.items():
        if info['disponivel']:
            print(f'- {nome_item}: R$ {info["preco"]}')

    while True:
        pedido = input('\nDigite o item (ou "fim" para encerrar): ')
        
        if pedido == 'fim':
            break
        
        if pedido not in cardapio:
            print('Item nao existe no cardapio')
            continue
        
        if not cardapio[pedido]['disponivel']:
            print('Item indisponivel')
            continue
        
        print(f'✔ {pedido} adicionado!')
        itens_escolhidos.append(pedido)

    total = calcular_total({"itens": itens_escolhidos})
    print(f'\nTotal do pedido: R$ {total}')

    pago = input('Cliente pagou? (s/n): ')

    return {
        "cliente": nome,
        "itens": itens_escolhidos,
        "pago": pago == 's'
    }

def processar_dia(pedidos):
    for pedido in pedidos:
        valido, motivo = validar_pedido(pedido)

        if valido:
            desconto = 5 if pedido['pago'] else 0
            total = calcular_total(pedido, desconto=desconto)
            status = '✔ pago' if pedido['pago'] else '✘ não pago'
            print(f'[VÁLIDO]   {pedido["cliente"]} → R$ {total}  {status}')
        else:
            print(f'[INVÁLIDO] {pedido["cliente"]} → {motivo}')


pedidos_dia = []

while True:
    pedido = menu_interativo()
    pedidos_dia.append(pedido)

    continuar = input('\nProximo cliente? (s/n): ')
    if continuar == 'n':
        break

print('\n========== PROCESSANDO DIA ==========')
processar_dia(pedidos_dia)

print('\n========== RELATORIO DO DIA ==========')
relatorio = gerar_relatorio(pedidos_dia)

print(f'Totais por cliente: {relatorio["total por cliente "]}')

if relatorio['clientes devedores']:
    print(f'Clientes devedores: {relatorio["clientes devedores"]}')

print(f'Categorias pedidas: {relatorio["categorias pedidas"]}')