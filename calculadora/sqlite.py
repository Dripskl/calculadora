import sqlite3

banco = sqlite3.connect('historico.db')

cursor = banco.cursor()


# cursor.execute('create table historico (numero1 real, numero2 real, op text)')
# cursor.execute('alter table historico add column total real')

#apagar historico
cursor.execute("DELETE FROM historico")
banco.commit()


"""
██████╗ ██████╗ ██╗██████╗──██████╗
██╔══██╗██╔══██╗██║██╔══██╗██╔════╝
██║  ██║██████╔╝██║██████╔╝╚█████╗
██║  ██║██╔══██╗██║██╔═══╝──╚═══██╗
██████╔╝██║  ██║██║██║─────██████╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝─────╚═════╝→
"""