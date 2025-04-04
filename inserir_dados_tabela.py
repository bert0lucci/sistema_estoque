import sqlite3

# Reabrir a conexão
banco = sqlite3.connect("meu_banco.db")
cursor = banco.cursor()

# Inserir dados
cursor.execute("INSERT INTO estoque (nome, quantidade) VALUES (?, ?)", 
               ("BRAHMA", 58))


# Confirmar as mudanças
banco.commit()
banco.close()
print("Dados inseridos com sucesso!")
