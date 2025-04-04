usuario = '478' #usuário cadastrado
bebidas = []
alimentos = [] 
contas = []

print("Digite seu CPF")
    
while True:
    login = input("Login: ")

    if login == usuario:
        print("------------------- Bem-vindo ao sistema da sede da divisão Bauru do Insanos MC --------------------")
        break
    else :
        print("Login não encontrado, tente novamente.") 

print("Selecione uma opção para acessar.")
op = input("\n1-Consulta Estoque\n2-Cadastro no Sistema\n")


while True:
    if op == "1":
        import sqlite3

        # Conectar ao banco
        banco = sqlite3.connect("meu_banco.db")
        cursor = banco.cursor()

        # Buscar estoque
        cursor.execute("SELECT * FROM estoque")
        values = cursor.fetchall()

        # Exibir os dados
        print(values)

        # Fechar conexão
        banco.close()
        break

    elif op == 2:
    
        import sqlite3

        # Conectar ao banco
        banco = sqlite3.connect("meu_banco.db")
        cursor = banco.cursor()

        # Buscar todos os clientes
        cursor.execute("SELECT * FROM estoque")
        values = cursor.fetchall()

        # Exibir os dados
        print(values)

        banco.close()
        break

    else:
        print("Opção Inválida")




