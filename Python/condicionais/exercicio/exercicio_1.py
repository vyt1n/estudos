'''
Você vai criar um programa que decide o acesso a um sistema de jogos online com base em 
algumas regras. O programa deve:

Receber do usuário:

    - idade (número inteiro)
    - assinatura (string: "BASICO", "PREMIUM" ou "VIP")
    - aceitou_termos (boolean: True ou False)

Validar e aplicar as regras abaixo:

    - O usuário só pode entrar se aceitou os termos (aceitou_termos é True).
    - O usuário menor de 13 anos só pode entrar se tiver assinatura "VIP".
    - O usuário entre 13 e 17 anos pode entrar com assinatura "PREMIUM" ou "VIP".
    - O usuário com 18 anos ou mais pode entrar com qualquer assinatura.

Qualquer entrada inválida (como assinatura diferente das três opções) deve exibir uma 
mensagem de erro.

Ao final, o programa deve imprimir:

    - "Acesso permitido" se todas as condições forem atendidas.
    - "Acesso negado" caso alguma regra não seja satisfeita.
    - "Erro: assinatura inválida" se a assinatura não for uma das três válidas.
'''

idade = None
assinatura = None
aceitou_termos = None

idade = int(input('Digite sua idade: '))

if idade > 0:

    if idade < 13:
        print('usuário menor de 13 anos só pode entrar se tiver assinatura "VIP"')
        
        continuar = input('Deseja continuar? (s/n): ').lower().strip()
        if continuar[0] == 's':
            assinatura = 'VIP'
            print(f'Assinatura: {assinatura}')

            concordar = input('Concorda com os termos? (s/n): ').lower().strip()
            if concordar[0] == 's':
                aceitou_termos = True
                print('Acesso permitido')
            else:
                aceitou_termos = False
                print('Acesso negado')
                exit('\nPROGRAMA FINALIZADO!!!')

        else:
            print('Acesso Negada')
            exit('\nPROGRAMA FINALIZADO!!!')

    elif idade >= 13 and 17 <= idade:
        print('usuário entre 13 e 17 anos pode entrar com assinatura "PREMIUM" ou "VIP".')

        continuar = input('Deseja continuar? (s/n): ').lower().strip()
        if continuar[0] == 's':
            plano = input('Qual plano deseja: "PREMIUM" ou "VIP"').upper().strip()

            if plano == 'PREMIUM' or plano == 'VIP':
                assinatura = plano
                print(f'Assinatura: {assinatura}')

                concordar = input('Concorda com os termos? (s/n): ').lower().strip()
                if concordar[0] == 's':
                    aceitou_termos = True
                    print('Acesso permitido')
                else:
                    aceitou_termos = False
                    print('Acesso negado')
                    exit('\nPROGRAMA FINALIZADO!!!')

            else:
                print('Erro: assinatura inválida')
                exit('\nPROGRAMA FINALIZADO!!!')

        else:
            print('Acesso Negado')
            exit('\nPROGRAMA FINALIZADO!!!')

    else:
        plano = input('Qual plano deseja: "BASICO", "PREMIUM" ou "VIP"').upper().strip()
        if plano == 'BASICO' or plano == 'PREMIUM' or plano == 'VIP':
            assinatura = plano
            print(f'Assinatura: {assinatura}')

            concordar = input('Concorda com os termos? (s/n): ').lower().strip()
            if concordar[0] == 's':
                aceitou_termos = True
                print('Acesso permitido')
            else:
                aceitou_termos = False
                print('Acesso negado')
                exit('\nPROGRAMA FINALIZADO!!!')

        else:
            print('Erro: assinatura inválida')
            exit('\nPROGRAMA FINALIZADO!!!')       
        


    print(f'Idade: {idade}, assinatura: {assinatura}, termos aceitos: {aceitou_termos}')

else:
    print('Idade invalida')
    exit('\nPROGRAMA FINALIZADO!!!')