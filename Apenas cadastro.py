#Gustavo da Cunha Oliveira - 16/11/2023
#Fatec São Caetano do Sul - Projeto N2
#Cadastro de filmes em banco de dados, por código Python

import sqlite3   # Biblioteca do sqlite
conn = sqlite3.connect("TabelaFilmes.db")

while True:
    try:
        vcodigo = float(input("Digite o código do filme: "))
        break
    except ValueError:
        print("Formato de código inválido!")

vnome = input("Qual o nome do filme? ")

while True:
    vgenero = input("Qual o gênero do filme? ")
    if vgenero.isalpha():
        break
    else:
        print("Formato de gênero inválido!")

while True:
    try:
        vdata = float(input("Qual o dia que você viu esse filme? "))
        break
    except ValueError:
        print("Dia inválido!")

while True:
    try:
        vnota = float(input("Qual a nota do filme? "))
        break
    except ValueError:
        print("Nota inválida!")

while True:
    vconfirma = input("Confirma que deseja cadastrar? (S/N)")
    if vconfirma.upper() == "S" or vconfirma.upper() == "SIM":
        # Enviar instrução SQL para ser executada
        conn.execute("insert or ignore into filmes values(?, ?, ?, ?, ?)",(vcodigo,vnome,vgenero,vdata,vnota) )
        conn.commit()
        print("Filme cadastrado com sucesso!")
        break
    elif vconfirma.upper() == "N" or vconfirma.upper() == "NÃO":
        print("Cadastro cancelado!")
        break
    else:
        print("Insira uma resposta válida") 

conn.close
quit()

