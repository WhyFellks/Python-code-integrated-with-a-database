#Gustavo da Cunha Oliveira - 16/11/2023
#Fatec São Caetano do Sul - Projeto N2
#Cadastro de filmes em banco de dados, por código Python

import sqlite3   # Biblioteca do sqlite
conn = sqlite3.connect("TabelaFilmes.db")
cursor = conn.cursor()

print("\n========== Cadastro de Filme ==========\n")

while True:
    try:
        vcodigo = float(input("Digite o código do filme: "))
        break
    except ValueError:
        print("\nFormato de código inválido!\n")

vnome = input("Qual o nome do filme? ")

while True:
    vgenero = input("Qual o gênero do filme? ")
    if vgenero.isalpha():
        break
    else:
        print("\nFormato de gênero inválido!\n")

while True:
    try:
        vdata = float(input("Qual o dia que você viu esse filme? "))
        break
    except ValueError:
        print("\nDia inválido!\n")

while True:
    try:
        vnota = float(input("Qual a nota do filme? "))
        break
    except ValueError:
        print("\nInsira uma nota válida!\n")

while True:
    vconfirma = input("Confirma que deseja cadastrar? (S/N)")
    if vconfirma.upper() == "S" or vconfirma.upper() == "SIM":
        # Enviar instrução SQL para ser executada
        conn.execute("insert or ignore into filmes values(?, ?, ?, ?, ?)",(vcodigo,vnome,vgenero,vdata,vnota) )
        conn.commit()
        print("\nFilme cadastrado com sucesso!")
        print("\n" * 26)
        break
    elif vconfirma.upper() == "N" or vconfirma.upper() == "NÃO":
        print("\nCadastro cancelado!")
        print("\n" * 26)
        break
    else:
        print("\nInsira uma resposta válida\n") 

while True:
    while True:
        try:
            print("O que você deseja?\n")
            print("Pesquisar filme por código - 1")
            print("Listar todos os filmes salvos - 2")
            print("\n" * 4)

            vescolha = float(input("\nSua resposta (Escolha 1 ou 2): "))
            print("\n" * 32)
            break
        except ValueError:
            print("\nInsira apenas o número 1 ou 2!!!")

    
    if vescolha == 1:
        print("\n" * 5)
        vcodigo = str(input("Qual o código do filme que você deseja pesquisar? "))
        cursor.execute("Select codigo, nome, genero, data, nota from filmes where codigo = " + vcodigo)
        rs = cursor.fetchone()
        if rs is not None:
            print ("\nFilme Encontrado")
            print ("Nome: ", rs[1])
            print ("Gênero: ", rs[2])
            print ("Data: ", rs[3])
            print ("Nota: ", rs[4])
    
        else:
            print("Código informado não existe")
        break

    elif vescolha == 2:
        cursor.execute("Select codigo, nome, genero, data, nota from filmes")
        resultados = cursor.fetchall()
        if len(resultados) > 0:
            print("\nLista de Filmes:")
            for rs in resultados:
                print("\nCódigo:", rs[0])
                print("Nome:", rs[1])
                print("Gênero:", rs[2])
                print("Data:", rs[3])
                print("Nota:", rs[4])
        else:
            print("Nenhum filme encontrado")
        break

while True:        
    vconfirma = input("\nDeseja excluir algum filme da lista? (S/N) ") 
    if vconfirma.upper() == "S" or vconfirma.upper() == "SIM":
        
        vexcluir = input("\nQual o código do filme que você deseja excluir? ")
        conn.execute("delete from filmes where codigo = " + vexcluir)
        conn.commit()
        print("\nFilme excluído com sucesso!")
        print("\n" * 36)
        break
    elif vconfirma.upper() == "N" or vconfirma.upper() == "NÃO":
        print("\nNenhum filme excluído")
        print("\n" * 36)
        break
    else:
        print("\nInsira uma resposta válida")

while True:
    valterar = input("Deseja alterar a nota de algum filme? (S/N) ")
    if valterar.upper() == "S" or valterar.upper() == "SIM":
        while True:
            try:
                vcodigo_alterar = float(input("\nQual o código do filme que você deseja alterar a nota? "))
                break
            except ValueError:
                print("\nInsira um código válido\n")

        while True:
            try:
                vnova_nota = float(input("Qual a nota que você deseja colocar? "))
                break
            except ValueError:
                print("\nInsira um valor válido\n")

        cursor.execute("UPDATE filmes SET nota = ? WHERE codigo = ?", (vnova_nota, vcodigo_alterar))
        conn.commit()
        print("\nNota atualizada com sucesso!")
        break

    elif valterar.upper() == "N" or valterar.upper() == "NÃO":
        print("\nNenhuma nota alterada")
        break

    else:
        print("Insira um valor válido")

conn.close
quit()

