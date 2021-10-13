class Carro:
    velMax=0
    ligado=False
    cor=""

    def __init__(self,v,l,c):
        self.velMax=v
        self.ligado=l
        self.cor=c
    
    def mostrar(self):
        print(f"Velocidade Máxima: {self.velMax}")
        print(f"Cor..............: {self.cor}")
        estado="Sim" if self.ligado else "Não"
        print(f"Ligado...........: {estado}")
        self.andando()
        print("-="*45)

    def ligar(self):
        self.ligado=True
    def desligar(self):
        self.ligado=False

    def andando(self):
        if(self.ligado):
            print("Andando")
        else:
            print("Parado")


c1=Carro(253,True,"Verde")
c1.mostrar()

c2=Carro(150,False,"Preto")
c2.mostrar()
c2.ligar()