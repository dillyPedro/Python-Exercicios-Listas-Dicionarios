dia = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))
ano = int(input('Digite o ano: '))

# Verificando se o mês e o ano são válidos:
if((1 <= mes <= 12) and (ano >= 0)):
    # Segue normalmente;

    # Descobrir o limite de dias para cada mês:
    if(mes in [1, 3, 5, 7, 8, 10, 12]):
        limite_dias = 31
    elif(mes in [4, 6, 9, 11]):
        limite_dias = 30
    else: # Se não for nenhum desses, o mês será o 2 (Fevereiro)

    # Analisando como fevereiro funciona:
        if(((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0)):
            limite_dias = 29
        else:
            limite_dias = 28

    # Verificar se o dia digitado está dentro dos limites:
    
    if (1 <= dia <= limite_dias):
        print(f'Data Atual = {dia}/{mes}/{ano}')
    else:
        print('Data incorreta!')
