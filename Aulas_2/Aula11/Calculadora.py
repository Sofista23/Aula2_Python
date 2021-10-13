def calculadora(x,y,alg):
    if(alg=="+"):
        r=x+y
        print(f"A soma entre {x} e {y} é {r}!")
    elif(alg=="-"):
        if(x>y):
            r=x-y
        elif(x==y):
            r=y-x
        else:
            r=y-x
        print(f"A diferença entre {x} e {y} é {r}!")
    elif(alg=="*"):
        r=x*y
        print(f"O produto entre {x} e {y} é {r}!")
    elif(alg=="/"):
        if(y==0):
            print("Impossível dividir algo por 0!")
        else:
            r=x/y
            print(f"O resultado da divisão entre {x} e {y} é {r}!")
    else:
        print("Dados fornecidos inválidos!")