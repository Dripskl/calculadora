import sqlite3
import os

#banco de dados start
banco = sqlite3.connect('historico.db')
cursor = banco.cursor()
#banco de dados end

# funçao de salvar operaçao
def salvar_operacao(numero1, numero2, op, resultado):
    salvar = input('Deseja salvar esta operação? (S/N): ').strip().upper()
    if salvar == 'S':
        cursor.execute(
            "INSERT INTO historico (numero1, numero2, op, total) VALUES (?, ?, ?, ?)",
            (numero1, numero2, op, resultado)
        )
        banco.commit()
        os.system('cls')
        print('Operação salva com sucesso!\n')

# Calcular
def calcular():
    numero1 = float(input('Digite o primeiro numero: '))
    numero2 = float(input('Digite o segundo numero: '))
    op = input('Digite um operador valido (+,-): ')
    if op == '+':
        operacao = numero1 + numero2
        print(f'O resultado da operaçao e: {operacao:.2f}')
        salvar_operacao()
    elif op == '-':
        operacao = numero1 - numero2
        print(f'O resultado da operaçao e: {operacao:.2f}')
        salvar_operacao()
    else:
        print('Digite um operador valido')
        return
    
    banco.commit() 

# Consultar Historico
def historico():
    cursor.execute("SELECT * FROM historico")
    resultados = cursor.fetchall()
    if resultados:
        for row in resultados:
            print(f"{row[0]} {row[2]} {row[1]} = {row[3]}")
            print("==================================")
    else:
        print("O histórico está vazio!\n\n")

# Apagar historico
def apagarhistorico():
    certeza = input('Tem certeza que deseja apagar o historico?(S/N): ')
    if certeza == 'S' or certeza == 's':
        certeza = input('Realmente vc tem certeza?(S/N): ')
        if certeza == 'S' or certeza == 's':
            cursor.execute('DELETE from historico')
            os.system('cls')
    banco.commit() 

        


"""
██████╗ ██████╗ ██╗██████╗──██████╗
██╔══██╗██╔══██╗██║██╔══██╗██╔════╝
██║  ██║██████╔╝██║██████╔╝╚█████╗
██║  ██║██╔══██╗██║██╔═══╝──╚═══██╗
██████╔╝██║  ██║██║██║─────██████╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝─────╚═════╝→
"""