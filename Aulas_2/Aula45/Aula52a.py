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

id=int(input("ID para CONSULTAR ou TODOS[000]: "))

if(id==000):
    vsql=f"SELECT * FROM contatos"
else:
    vsql=f"SELECT * FROM contatos WHERE id={id}"

#Consultar DATAS 
def consulta(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    res=c.fetchall()
    return res

print(consulta(vcon,vsql))

vcon.close()