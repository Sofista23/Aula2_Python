import os
carros=[]

class Carro:
    nome=""
    pot=0
    velMax=0
    ligado=False

    def __init__(self,nome,pot):
        self.nome=nome
        self.pot=pot
        self.velMax=pot*2
        self.ligado=False
    
    def ligar(self):
        self.ligado=True
    def desligar(self):
        self.ligado=False

    def info(self):
        print(f"Nome.............: {self.nome}")
        print(f"Potência.........: {self.pot}")
        print(f"Velocidade Máxima: {self.velMax}")
        print(f"Ligado?..........: {'sim' if self.ligado==True else 'não'}")



def menu():
    os.system("cls") or None
    print("1 - Novo Carro")
    print("2 - Informações do Carro")
    print("3 - Excluir Carro")
    print("4 - Ligar Carro")
    print("5 - Desligar Carro")
    print("6 - Listar Carro")
    print("7 - Sair")
    print(f"Quantidade de Carros: {len(carros)}")

    opc=int(input("Digite uma opção: "))
    return opc



def novoCarro():
    os.system("cls") or None

    n=input("Nome do Carro: ")
    p=input("Potência do Carro: ")

    car=Carro(n,p)

    carros.append(car)

    print("Carro Criado!")

    os.system("pause")



def informacoes():
    os.system("cls") or None
    n=int(input("Digite o número do Carro: "))
    try:
        carros[n].info()
    except:
        print("Carro não encontrado")
    os.system("pause")



def excluirCarro():
    os.system("cls") or None
    n=int(input("Digite o número do Carro: "))
    try:
        del carros[n]
    except:
        print("Carro não encontrado")
    os.system("pause")



def ligarCarro():
    os.system("cls") or None
    n=int(input("Digite o número do Carro: "))
    try:
        carros[n].ligar()
        print("Carro Ligado")
    except:
        print("Carro não encontrado")
    os.system("pause")



def desligarCarro():
    os.system("cls") or None
    n=int(input("Digite o número do Carro: "))
    try:
        carros[n].desligar()
        print("Carro Desigado")
    except:
        print("Carro não encontrado")
    os.system("pause")



def listarCarro():
    os.system("cls") or None
    p=0

    for c in carros:
        print("{p} - {c.nome}")
        p+=1



ret=menu()
while(ret<7):
    if(ret==1):
        novoCarro()
    elif(ret==2):
        informacoes()
    elif(ret==3):
        excluirCarro()
    elif(ret==4):
        ligarCarro()
    elif(ret==5):
        desligarCarro()
    elif(ret==6):
        listarCarro()
    ret=menu()

os.system("cls") or None

print("Programa finalizado")