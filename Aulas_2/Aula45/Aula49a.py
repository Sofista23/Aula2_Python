import sqlite3
from sqlite3 import Error

#Criar Conexão
def conexaoBanco():
    path="C:\\Users\\João Pedro Martins\\Documents\\PROGRAMAÇÃO\\Python\\Aulas_2\\Aula45\\Agenda.db"
    con=None

    try:
        con=sqlite3.connect(path)
    except Error as ex:
        print(ex)

    return con


vcon=conexaoBanco()


nome=input("Nome: ")
tel=input("Telefone: ")
em=input("Email: ")

vsql="INSERT INTO contatos(nome,telefone,email)VALUES('"+nome+"','"+tel+"','"+em+"')"

#Inserindo DATAS
def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Dados Registrados!")
    except Error as ex:
        print(ex)

inserir(vcon,vsql)

vcon.close()