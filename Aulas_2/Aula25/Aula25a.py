class NPC: #Classe Pai
    def __init__(self,nome,time,forca):
        self.nome=nome
        self.time=time
        self.forca=forca
        self.vivo=True
        self.vida=100

    def info(self):
        print(f"Nome: {self.nome}")
        print(f"Time: {self.time}")
        print(f"Força: {self.forca}")
        print(f"Vivo?: {'sim' if self.vivo else 'não'}")
        print(f"Vida: {self.vida}")
        print("-="*45)

class Soldado(NPC):
    def __init__(self, nome, time):
        self.forca=200
        super().__init__(nome,time,self.forca)
        super().info()

class Medico(NPC):
    def __init__(self, nome, time):
        self.forca=100
        super().__init__(nome,time,self.forca)

    def inf(self):
        super().info()


s1=Soldado("Peixe-Morto",1)
s2=Soldado("Olho-Frouxo",2)
s3=Medico("Melhor-Morrer",1)

s1.info()
s2.info()
s3.inf()