'''
## 🏕️ Mini Projeto — *Sistema de Seleção para uma Expedição*

### Contexto

Uma guilda de aventureiros precisa montar uma equipe para uma expedição perigosa. Você é o sistema responsável por **cadastrar candidatos, analisar os dados e decidir quem vai na missão**.

---

### O Problema

A guilda recebe fichas de candidatos com os seguintes dados:

- **Nome** (string)
- **Classe** (string: `"guerreiro"`, `"mago"`, `"arqueiro"`, `"curandeiro"`)
- **Nível** (int: 1 a 100)
- **Habilidades** (lista de strings)
- **Disponível** (bool)

A expedição exige que a equipe selecionada:

1. Tenha **no mínimo** um `curandeiro`
2. Tenha **no máximo** 4 membros
3. Cada membro deve ter **nível ≥ 30** e estar **disponível**
4. A equipe não pode ter **classes repetidas**
5. O sistema deve calcular o **nível médio** da equipe final
6. Deve listar todas as **habilidades únicas** da equipe (sem repetição)

---

### O que você precisa implementar

**1. Uma função `cadastrar_candidato`**
Recebe `nome`, `classe`, `nivel`, `disponivel` e `*habilidades`.
Retorna um dicionário com todos esses dados.

**2. Uma função `candidato_valido`**
Recebe um candidato e retorna `True` ou `False` dependendo se ele atende aos critérios básicos (nível ≥ 30 e disponível).

**3. Uma função `montar_equipe`**
Recebe a lista de todos os candidatos válidos e retorna uma lista com a equipe selecionada, respeitando as regras de classe única e limite de 4 membros.

**4. Uma função `relatorio_expedicao`**
Recebe a equipe montada e **kwargs opcionais** (ex: `nome_missao`, `destino`).
Imprime um relatório com: membros, nível médio, habilidades únicas e os kwargs passados.

**5. Uma função `verificar_equipe`**
Verifica se a equipe tem pelo menos um curandeiro. Retorna uma tupla `(bool, str)` — o bool indica se está apta, e a string explica o motivo.

---

### Dados de teste pra você usar

```python
candidatos_brutos = [
    ("Aldric", "guerreiro", 45, True, "escudo", "investida", "provocar"),
    ("Lyria", "maga", 28, True, "bola de fogo", "escudo arcano"),
    ("Thorn", "arqueiro", 55, False, "tiro preciso", "furtividade"),
    ("Mira", "curandeira", 40, True, "cura", "bênção", "ressurreição"),
    ("Brom", "guerreiro", 33, True, "investida", "golpe pesado"),
    ("Sylva", "arqueira", 60, True, "tiro preciso", "armadilha", "furtividade"),
    ("Cael", "mago", 70, True, "relâmpago", "bola de fogo", "teletransporte"),
    ("Rena", "curandeira", 22, True, "cura", "bênção"),
]
```

---

### Resultado esperado (aproximado)

```
=== RELATÓRIO DE EXPEDIÇÃO ===
Missão: Ruínas de Valdor
Destino: Floresta Sombria

Equipe selecionada:
  - Aldric (guerreiro) | Nível 45
  - Mira (curandeira)  | Nível 40
  - Sylva (arqueira)   | Nível 60
  - Cael (mago)        | Nível 70

Nível médio da equipe: 53.75
Habilidades únicas: {'escudo', 'investida', 'provocar', 'cura', 'bênção', 'ressurreição', 'tiro preciso', 'armadilha', 'furtividade', 'relâmpago', 'bola de fogo', 'teletransporte'}

Status: ✅ Equipe apta para a expedição!
```

---

### Dicas sem entregar a resposta

- `*habilidades` dentro de uma função vira uma **tupla** — pensa em como transformá-la numa lista no dicionário
- Para garantir classes únicas, pensa em **qual estrutura de dado naturalmente não repete elementos**
- `**kwargs` no relatório é só um dicionário que você itera normalmente com `.items()`
- A tupla de retorno em `verificar_equipe` é `return True, "mensagem"` — simples assim

'''

def cadastrar_candidato():
    dados_candidato = {}
    while True:
        nome = input('Nome do candidato: ').strip().title()
        if nome == '':
            print('Nome vazio. Tente novamente')
            continue
        dados_candidato.update({'nome': nome})
        break
    
    classes_disponiveis = ("guerreiro", "mago", "arqueiro", "curandeiro", "guerreira", "maga", "arqueira", "curandeira")
    while True:
        classe = input(f'classe do candidato {classes_disponiveis}: ').strip().lower()
        if classe == '':
            print('Classe vazia. Tente novamente')
            continue
        elif classe not in classes_disponiveis: 
            print('Classe invalida. Tente novamente')
            continue
        dados_candidato.update({'classe': classe})
        break
    
    while True:
        nivel_str = (input('Nivel do candidato: '))
        if nivel_str == '':
            print('Nivel vazio. Tente novamente')
            continue
        nivel = int(nivel_str)
        if nivel < 1:
            print('nivel invalido. Tente novamente')
            continue
        dados_candidato.update({'nivel': nivel})
        break
    
    habilidades_listadas = []
    while True:
        habilidades = input('Habilidade do candidato: ').strip().lower()
        if habilidades == '':
            print('Habilidades vazia. Tente novamente')
            continue
        habilidades_listadas.append(habilidades)
        continua = ''
        while True:
          continua = input('Deseja adicionar mais alguma habilidade? (s/n): ').strip().lower()
          if continua != 's' and continua != 'n':
              print('Opcao invalida. Tente novamente')
          else:
              break 
        if continua == 'n':
            dados_candidato.update({'habilidade': habilidades_listadas})
            break

    while True:
        disponibilidade = input('Disponivel? (s/n): ').strip().lower()
        if disponibilidade != 's' and disponibilidade != 'n':
            print('disponibilidade invalida. Tente novamente')
            continue
        disponivel = disponibilidade == 's'
        dados_candidato.update({'disponivel': disponivel})
        break

    return dados_candidato

def candidato_valido(candidatos):
    candidatos_validos = []
    for validacao in candidatos:
        if validacao['nivel'] >= 30 and validacao['disponivel'] == True:
            candidatos_validos.append(validacao)

    return candidatos_validos

def montar_equipe(candidatos_validos):
    equipe_montada = []
    classes = set()

    for regras in candidatos_validos:
        if regras['classe'] not in classes:
            classes.add(regras['classe'])
            if len(equipe_montada) < 4:
                equipe_montada.append(regras)
            else:
                break
    
    return equipe_montada

def relatorio_expedicao(equipe_montada, **kwargs):
    print('=== RELATÓRIO DE EXPEDIÇÃO ===')

    print(f"Missão: {kwargs.get('missao')}")
    print(f"Destino: {kwargs.get('destino')}")

    print('\nEquipe selecionada: ')
    media_nivel = 0
    habilidades_unicas = set()
    for equipe in equipe_montada:
        print(f"- {equipe['nome']} ({equipe['classe']}) | nivel {equipe['nivel']}")
        media_nivel += equipe['nivel']
        habilidades_unicas.update(equipe['habilidade'])

    print(f'\nNível médio da equipe: {(media_nivel / len(equipe_montada)):.2f}')
    print(f'Habilidades unicas: {habilidades_unicas}')

def verificar_equipe(equipe_montada):
    status = False
    for verificacao in equipe_montada:
        if verificacao['classe'] in ('curandeira', 'curandeiro'):
            status = True
            print(f'\nStatus: {status}. Equipe apta para a expedição!')
            return status
        
    print(f'\nStatus: {status}. Equipe nao está apta para a expedição!')
    return status
        
qtd_candidatos = int(input('Quantos candidatos serao avaliados? '))

candidatos = []
for i in range(qtd_candidatos):
    print(f'candidato {i + 1}: ')
    candidato = cadastrar_candidato()
    candidatos.append(candidato)

validacao_candidato = candidato_valido(candidatos)

equipe_montada = montar_equipe(validacao_candidato)

relatorio_expedicao(equipe_montada, missao='Ruínas de Valdor', destino='Floresta Sombria')

verificar_equipe(equipe_montada)