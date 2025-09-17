from func import *  # importa todas as funções do arquivo func.py
import os

os.system('cls')  # limpa a tela do terminal

while True:
    # menu principal da calculadora
    controle = int(input('\n--------Calculadora--------\n----------------------------\n1. Acessar a calculadora \n-\n2. Acessar o historico \n-\n0. Sair\n----------------------------\nDigite: '))
    
    if controle == 0:
        os.system('cls')
        print('Ate mais...')
        break  # encerra o programa
    elif controle == 1:
        calcular()  # chama a função de cálculo
    elif controle == 2:
        os.system('cls')
        # menu do histórico
        controle_historico = int(input('--------Historico--------\n----------------------------\n1. Consultar historico\n-\n2. Apagar historico\n-\n0. voltar\n----------------------------\nDigite: '))
        if controle_historico == 1:
            os.system('cls')
            print('\n--------Historico--------')
            historico()  # mostra o histórico
        elif controle_historico == 2:
            os.system('cls')
            apagarhistorico()  # apaga o histórico



"""
██████╗ ██████╗ ██╗██████╗──██████╗
██╔══██╗██╔══██╗██║██╔══██╗██╔════╝
██║  ██║██████╔╝██║██████╔╝╚█████╗
██║  ██║██╔══██╗██║██╔═══╝──╚═══██╗
██████╔╝██║  ██║██║██║─────██████╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝─────╚═════╝→

"""
