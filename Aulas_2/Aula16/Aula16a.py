m=input("Digite o Modelo: ")
f=input("Digite o Fabricante: ")
a=int(input("Digite o Ano: "))

carros=[
    ["Modelo:",m],
    ["Fabricante:",f],
    ["Ano:",a]
]

print("-="*30)

for x,y in carros:
    print(x,y)