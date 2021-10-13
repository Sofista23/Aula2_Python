def somar(x,y):
    print("-="*35)
    print(f"A soma entre {x} e {y} é {x+y}")
    print("-="*35)

def subtrair(x,y):
    print("-="*35)
    print(f"A diferença entre {x} e {y} é {x-y}")
    print("-="*35)

def calculos():
    n1=float(input("Diguite um número: "))
    n2=float(input("Diguite outro número: "))

    somar(n1,n2)
    subtrair(n1,n2)

calculos()




def textos(*txt):
    for x in txt:
        print(x)

textos("Taiga","Ryuji","Minori","Ami")




def soma(a,b):
    return a+b

n1=int(input("Digite um número: "))
n2=int(input("Digite outro número: "))

print(f"A soma entre {n1} e {n2} é {soma(n1,n2)}")