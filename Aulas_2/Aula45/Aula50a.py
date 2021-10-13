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

id=int(input("ID para DELETAR: "))

vsql=f"DELETE FROM contatos WHERE id={id}"

#Deletando DATAS 
def deletar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Dados Deletados!")
    except Error as ex:
        print(ex)

deletar(vcon,vsql)

vcon.close()