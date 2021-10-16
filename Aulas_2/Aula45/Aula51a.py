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

id=int(input("ID para ATUALIZAR: "))

esc=input("Nome[n] / Telefone[t] / Email[e]: ").upper().strip()

if(esc=="N"):
    dado=input("Nome: ")
    vsql=f"UPDATE contatos SET nome='{dado}' WHERE id={id}"

if(esc=="T"):
    dado=input("Telefone: ")
    vsql=f"UPDATE contatos SET telefone='{dado}' WHERE id={id}"

if(esc=="E"):
    dado=input("Email: ")
    vsql=f"UPDATE contatos SET email='{dado}' WHERE id={id}"

#Update DATAS 
def atualizar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Dados Atualizados!")
    except Error as ex:
        print(ex)

atualizar(vcon,vsql)

vcon.close()