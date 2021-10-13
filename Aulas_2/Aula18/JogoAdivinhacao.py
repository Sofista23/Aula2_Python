from random import randint

while True:
    print("-="*35)

    print("Jogo da Adivinhação!")

    print("-="*35)

    num=int(input("Digite um número de 0 a 10: "))

    print("-="*35)

    comp=randint(0,11)

    print(f"Você: {num}")
    print(f"Computador: {comp}")

    print("-="*35)

    if(num==comp):
        print("Acertou!!!")
    else:
        print("Errou!!!")

    print("-="*35)

    esc=input("Continua[s/n]: ").upper()
    if(esc=="N"):
        print("-="*35)
        break