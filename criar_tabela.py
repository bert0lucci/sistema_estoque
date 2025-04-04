import sqlite3

# Conectar ao banco (ou criar um novo arquivo)
banco = sqlite3.connect("meu_banco.db")
cursor = banco.cursor()

# Criar a tabela (se não existir)
cursor.execute('CREATE TABLE IF NOT EXISTS estoque (nome text, quantidade number)')
 

# Confirmar e fechar conexão
banco.commit()
banco.close()
print("Tabela criada com sucesso!")
