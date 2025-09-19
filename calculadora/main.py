from func import *
import os
os.system('cls')
while True:
    controle = int(input('\n--------Calculadora--------\n----------------------------\n1. Acessar a calculadora \n-\n2. Acessar o historico \n-\n0. Sair\n----------------------------\nDigite: '))
    if controle == 0:
        os.system('cls')
        print('Ate mais...')
        break
    elif controle == 1:
        calcular()
    elif controle == 2:
        os.system('cls')
        controle_historico = int(input('--------Historico--------\n----------------------------\n1. Consultar historico\n-\n2. Apagar historico\n-\n0. voltar\n----------------------------\nDigite: '))
        if controle_historico == 1:
            os.system('cls')
            print('\n--------Historico--------')
            historico()
        elif controle_historico == 2:
            os.system('cls')
            apagarhistorico()
        elif controle_historico == 0:
            os.system('cls')
        


"""
██████╗ ██████╗ ██╗██████╗──██████╗
██╔══██╗██╔══██╗██║██╔══██╗██╔════╝
██║  ██║██████╔╝██║██████╔╝╚█████╗
██║  ██║██╔══██╗██║██╔═══╝──╚═══██╗
██████╔╝██║  ██║██║██║─────██████╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝─────╚═════╝
"""
