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

#Criar Table
vsql="""CREATE TABLE contatos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(30),
    telefone VARCHAR(14),
    email VARCHAR(30)
)"""


def criarTable(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela criada!")
    except Error as ex:
        print(ex)


criarTable(vcon,vsql)

vcon.close()