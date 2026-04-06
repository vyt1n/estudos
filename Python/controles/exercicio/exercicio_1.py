'''
Desafio: Portal de acesso da Arena Nexus

Crie um programa que controle o acesso de usuários a uma arena de jogos.

O programa deve:

    receber idade como número inteiro
    receber assinatura como string
    receber aceitou_termos como booleano
    usar if, elif, else, and, or, not
    usar while, for, range() e break

Regras de acesso:

    O usuário só entra se tiver aceitado os termos.
    Se tiver menos de 13 anos, só entra com assinatura VIP.
    Se tiver entre 13 e 17 anos, entra com PREMIUM ou VIP.
    Se tiver 18 anos ou mais, entra com qualquer assinatura válida.
    Assinaturas válidas são apenas: BASICO, PREMIUM, VIP.

Parte com loop

O usuário terá 3 tentativas para digitar uma assinatura válida:

    Se digitar uma assinatura inválida, o programa deve avisar e permitir tentar de novo.
    Se acertar antes das 3 tentativas, pare o loop com break.
    Se errar nas 3, mostre: Erro: assinatura inválida

Saídas possíveis

O programa deve terminar exibindo apenas uma dessas mensagens finais:

    Acesso permitido
    Acesso negado
    Erro: assinatura inválida

O que eu quero que o programa faça:

    Pergunte a idade.
    Pergunte se aceitou os termos.
    Se não aceitou, negar acesso imediatamente.
    Se aceitou, pedir a assinatura.
    Dar até 3 tentativas para uma assinatura válida.
    Se a assinatura for válida, aplicar a regra da idade.
    Mostrar o resultado final.

Desafio bônus

Depois de terminar, tente fazer uma versão que use:

    um while para controlar as tentativas
    um for range(3) para repetir as tentativas
    e break quando a assinatura for válida
'''


idade = int(input('Digite sua idade: '))

if idade < 0:
    print('Idade invalida')

else:
    termo = input('Aceita os termos e contrato? (s/n): ').lower().strip()

    if termo == 'n':
        print('Acesso negado')

    else:
        assinatura_valida = False
        assinatura = ''

        for plano in range(3):
            assinatura = input('Qual assinatura deseja contratar (BASICO, PREMIUM ou VIP): ').upper().strip()

            if assinatura == 'BASICO' or assinatura == 'PREMIUM' or assinatura == 'VIP':
                assinatura_valida = True
                break

            elif plano < 2:
                print('Erro: assinatura inválida')
            
            else:
                break

        if assinatura_valida:

            if idade < 13:
                if assinatura != 'VIP':
                    print('Usuarios menores de 13 anos só é permitido a assinatura do "VIP"')
                    print('Acesso negado')

                else:
                    print('Acesso permitido')  

            elif idade > 12 and idade < 18:
                if assinatura != 'VIP' and assinatura != 'PREMIUM':
                    print('Usuarios entre 13 a 17 anos só é permitido a assinatura do "VIP" ou "PREMIUM"')
                    print('Acesso negado')
                
                else:
                    print('Acesso permitido')

            else:
                print('Acesso permitido')

        else:
            print('Erro: assinatura inválida')