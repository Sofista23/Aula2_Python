import re  #RegEx Divisão

txt="Toradora - Taiga e Ryuji"

res=re.split(" ",txt)

print(res)

for x in res:
    print(x)