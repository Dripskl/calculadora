import sqlite3
import os

# Conecta ao banco de dados SQLite 'historico.db' e cria o cursor
banco = sqlite3.connect('historico.db')
cursor = banco.cursor()

# Função para salvar uma operação no histórico se o usuário quiser
def salvar_operacao(numero1, numero2, op, resultado):
    salvar = input('Deseja salvar esta operação? (S/N): ').strip().upper()
    if salvar == 'S':
        cursor.execute(
            "INSERT INTO historico (numero1, numero2, op, total) VALUES (?, ?, ?, ?)",
            (numero1, numero2, op, resultado)
        )
        banco.commit()  # salva no banco
        os.system('cls')
        print('Operação salva com sucesso!\n')
    elif salvar == 'N':
        os.system('cls')
        print('Operaçao nao foi salva pela escolha do usuario! \n')

# Função para calcular soma ou subtração
def calcular():
    numero1 = float(input('Digite o primeiro numero: '))
    numero2 = float(input('Digite o segundo numero: '))
    op = input('Digite um operador valido (+,-, * e /): ')
    
    if op == '+':
        operacao = numero1 + numero2
        print(f'O resultado da operaçao e: {operacao:.2f}')
        salvar_operacao(numero1, numero2, op, operacao)  # chama função de salvar
    elif op == '-':
        operacao = numero1 - numero2
        print(f'O resultado da operaçao e: {operacao:.2f}')
        salvar_operacao(numero1, numero2, op, operacao)  # chama função de salvar
    elif op == '*':
        operacao = numero1 * numero2
        print(f'O resultado da operaçao e: {operacao:.2f}')
        salvar_operacao(numero1, numero2, op, operacao) # chama função de salvar
    elif op == '/':
        if numero2 == 0:
            print('Nao tem como dividir por zero')
        else:
            operacao = numero1 / numero2
            print(f'O resultado da operaçao e: {operacao:.2f}')
            salvar_operacao(numero1, numero2, op, operacao) # chama função de salvar
    else:
        print('Digite um operador valido')
        return
    
    banco.commit()  # confirma alterações no banco

# Função para consultar e mostrar o histórico
def historico():
    cursor.execute("SELECT * FROM historico")
    resultados = cursor.fetchall()
    if resultados:
        for row in resultados:
            print(f"{row[0]} {row[2]} {row[1]} = {row[3]}")
            print("==================================")
    else:
        print("O histórico está vazio!\n\n")

# Função para apagar todo o histórico, com confirmação dupla
def apagarhistorico():
    certeza = input('Tem certeza que deseja apagar o historico?(S/N): ')
    if certeza == 'S' or certeza == 's':
        certeza = input('Realmente vc tem certeza?(S/N): ')
        if certeza == 'S' or certeza == 's':
            cursor.execute('DELETE from historico')
            os.system('cls')
    banco.commit()  # aplica a exclusão


        


"""
██████╗ ██████╗ ██╗██████╗──██████╗
██╔══██╗██╔══██╗██║██╔══██╗██╔════╝
██║  ██║██████╔╝██║██████╔╝╚█████╗
██║  ██║██╔══██╗██║██╔═══╝──╚═══██╗
██████╔╝██║  ██║██║██║─────██████╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝─────╚═════╝→
"""
