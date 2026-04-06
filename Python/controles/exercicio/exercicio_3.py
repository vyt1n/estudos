'''
Uma empresa terceirizada de segurança digital criou um sistema simples, em Python, para decidir se um analista pode entrar na fila de atendimento de incidentes críticos.
O problema é que os dados chegam de forma incompleta, inconsistente e às vezes contraditória. Você precisa montar a lógica de decisão usando apenas os conteúdos das seções:

    tipos de dados
    estruturas lógicas
    loops


Cenário

O programa deve controlar a entrada de um analista em um plantão de emergência.

O sistema receberá:

    idade → número inteiro
    cargo → string
    tem_badge → boolean
    esta_na_empresa → boolean
    horario → string
    tentativa_login → string

Regras do caso

1) Regras de base

O analista só pode seguir para validação se:

    tiver tem_badge == True
    e estiver esta_na_empresa == True

Se qualquer uma dessas condições falhar, a pessoa deve ser bloqueada imediatamente.

2) Regras de cargo

Os cargos aceitos são apenas:

    "JUNIOR"
    "PLENO"
    "SENIOR"

Mas há uma exceção:

    Se a pessoa tiver menos de 21 anos, ela não pode ser "SENIOR".

3) Regras de horário

O campo horario pode vir com estes valores válidos:

    "MANHA"
    "TARDE"
    "NOITE"

Só que o comportamento muda assim:

    JUNIOR só entra de MANHA
    PLENO entra de MANHA ou TARDE
    SENIOR entra em qualquer horário válido

4) Tentativa de login

Antes de liberar o acesso, o programa deve validar a tentativa de login com até 3 tentativas.

A regra é:

    Se tentativa_login for diferente de "OK", o sistema deve permitir tentar novamente.
    Se acertar antes das 3 tentativas, parar o loop com break.
    Se errar as 3 vezes, encerrar com bloqueio.

Saídas possíveis

O programa deve terminar exibindo uma decisão final principal, que pode ser uma destas:

    "Acesso permitido"
    "Acesso negado"
    "Bloqueio por falha de autenticação"
    "Revisão manual necessária"

Condição especial de ambiguidade

Se os dados estiverem tecnicamente válidos, mas houver conflito entre idade, cargo e horário, você não deve simplesmente negar automaticamente.

Nesse caso, o programa pode optar por:

    negar o acesso
    ou encaminhar para "Revisão manual necessária"

desde que você justifique a lógica usada.

O que seu programa precisa fazer

Ler todos os dados.
Validar se a pessoa está dentro das condições mínimas.
Dar até 3 tentativas para o login.
Validar cargo, idade e horário.
Decidir o resultado final.
Mostrar apenas uma saída final principal.

O que eu quero na sua resposta

Depois de resolver, envie:

Parte 1 — Código

Seu programa em Python.

Parte 2 — Justificativa

Explique por que você organizou as validações nessa ordem.

Parte 3 — Riscos

Aponte pelo menos 2 riscos lógicos do seu próprio algoritmo.

Parte 4 — Alternativa

Mostre uma segunda forma de resolver o problema, mesmo que seja menos elegante.

Restrições

Use if, elif, else
Use AND, OR, NOT
Use while, for, range() e break
Não use funções
Não use listas, dicionários ou estruturas que ainda não estudamos

Desafio de nível profissional

Seu código deve lidar com pelo menos estes cenários:

    cargo inválido
    horário inválido
    idade incompatível com o cargo
    falha nas 3 tentativas de login
    dados válidos, mas decisão ambígua
'''

idade = int(input('Digite sua idade: '))

if idade < 0:
    print('Bloqueio por falha de autenticação')

else:
    badge = input('Tem badge? (s/n): ').lower().strip()
    tem_badge = badge == 's'

    empresa = input('Esta na empresa? (s/n): ').lower().strip()
    esta_na_empresa = empresa == 's'

    if not (tem_badge and esta_na_empresa):
        print('Bloqueio por falha de autenticação')

    else:
        validacao_cargo = False

        cargo = input('Qual é o seu cargo? ("JUNIOR", "PLENO" ou "SENIOR"): ').upper().strip()

        if idade < 21 and cargo == 'SENIOR':
            print('Revisão manual necessária')

        else:
            horario = input('Qual seu horario? ("MANHA", "TARDE" ou "NOITE"): ').upper().strip()

            if cargo == 'JUNIOR':
                if horario != 'MANHA':
                    print('Acesso negado')
                else:
                    validacao_cargo = True

            elif cargo == 'PLENO':
                if horario != 'MANHA' and horario != 'TARDE':
                    print('Acesso negado')
                else:
                    validacao_cargo = True

            else:
                    validacao_cargo = True
        
        if validacao_cargo:
            usuario = 'ViTin23'
        
            for i in range(3):
                login = input('Login: ')
                if login == usuario:
                    print('Acesso liberado')
                    break
                elif i < 2:
                    print('Usuario invalido. Tente novamente!')
                else:
                    print('excedeu o limite de tentativas')
                    print('Bloqueio por falha de autenticação')
                
        
            
        






