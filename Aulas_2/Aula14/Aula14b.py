nomes=[]
nome=input("Digite o nome: ")

while(nome!="-1"):
    nomes.append(nome)
    nome=input("Digite o nome: ")

for x in nomes:
    print(x)