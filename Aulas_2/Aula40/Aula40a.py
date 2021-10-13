import re  #RegEx

txt="Toradora - Taiga e Ryuji"

print(f"Texto: '{txt}'")

esc=input("O que quer procurar na frase?: ")

res=re.findall(esc,txt)

quant=res.count

print(res)

print(f"Quantidade de Elementos Encontrados: {quant}")