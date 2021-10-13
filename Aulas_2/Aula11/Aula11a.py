from Calculadora import calculadora

while True:
    n1=float(input("Digite um número: "))
    n2=float(input("Digite outro número: "))
    op=input("Soma[+], Subtração[-], Multiplicação[*] e Divisão[/]: ").strip()

    calculadora(n1,n2,op)

    esc=input("Continuar[s/n]: ").upper().strip()
    if(esc=="N"):
        break