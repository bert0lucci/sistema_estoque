import sqlite3

# Conectar ao banco
banco = sqlite3.connect("meu_banco.db")
cursor = banco.cursor()

# Buscar todos os clientes
cursor.execute("SELECT * FROM estoque")
values = cursor.fetchall()

# Exibir os dados
print(values)

# Fechar conexão
banco.close()