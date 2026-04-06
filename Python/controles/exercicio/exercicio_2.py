'''
Exercício — Sistema de liberação de sala de estudo

Uma biblioteca possui salas de estudo com regras de acesso.

O programa deve:

Entradas:

    idade → número inteiro
    possui_carteirinha → boolean (True ou False)
    periodo → string ("MANHA", "TARDE", "NOITE")

Regras:

    O usuário só pode entrar se possuir carteirinha.
    Menores de 14 anos só podem entrar no período "MANHA".
    Usuários de 14 a 17 anos podem entrar "MANHA" ou "TARDE".
    Usuários com 18 anos ou mais podem entrar em qualquer período válido.

Períodos válidos são apenas:

    "MANHA"
    "TARDE"
    "NOITE"

Parte com loop

O usuário terá 3 tentativas para digitar um período válido:

    Se digitar errado, avisar "Período inválido"
    Se acertar, usar break

Se errar as 3 vezes, mostrar:

    Erro: período inválido

Saídas possíveis (somente estas no final):

    Acesso permitido
    Acesso negado
    Erro: período inválido

Requisitos obrigatórios

Seu código deve usar:

    if
    elif
    else
    AND
    OR
    NOT
    for
    range()
    break
    
Desafio bônus (opcional):

    Use uma variável booleana tipo periodo_valido
    Evite repetir print
    Faça as validações na ordem lógica correta
'''

idade = int(input('Digite sua idade: '))

possui_carteirinha = input('Possui carteirinha? (s/n): ').lower().strip()

if possui_carteirinha != 's':
    print('Acesso negado')

else:
    periodo_valido = False
    periodo = ''

    for tentativa in range(3):

        periodo = input('Qual periodo deseja ("MANHA", "TARDE" ou "NOITE"): ').upper().strip()

        if periodo == "MANHA" or periodo == "TARDE" or periodo == "NOITE":
            periodo_valido = True
            break

        if tentativa < 2:
            print('Erro: período inválido')

    if not periodo_valido:
        print('Acesso negado')

    else:
        if idade < 14:
            if periodo == 'MANHA':
                print('Acesso permitido')
            else:
                print('Acesso negado')

        elif 14 <= idade <= 17:
            if periodo == 'MANHA' or periodo == 'TARDE':
                print('Acesso permitido')
            else:
                print('Acesso negado')

        else:
            print('Acesso permitido')






# O usuário só pode entrar se possuir carteirinha.
# Menores de 14 anos só podem entrar no período "MANHA".
# Usuários de 14 a 17 anos podem entrar "MANHA" ou "TARDE".
# Usuários com 18 anos ou mais podem entrar em qualquer período válido