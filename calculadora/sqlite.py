import sqlite3

# Conecta ao banco de dados SQLite 'historico.db'
banco = sqlite3.connect('historico.db')
cursor = banco.cursor()

# Linhas comentadas mostram como criar tabela e adicionar coluna
# cursor.execute('create table historico (numero1 real, numero2 real, op text)')
# cursor.execute('alter table historico add column total real')

# Apaga todo o histórico da tabela
cursor.execute("DELETE FROM historico")
banco.commit()  # confirma a exclusão no banco


"""
██████╗ ██████╗ ██╗██████╗──██████╗
██╔══██╗██╔══██╗██║██╔══██╗██╔════╝
██║  ██║██████╔╝██║██████╔╝╚█████╗
██║  ██║██╔══██╗██║██╔═══╝──╚═══██╗
██████╔╝██║  ██║██║██║─────██████╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝─────╚═════╝→

"""
