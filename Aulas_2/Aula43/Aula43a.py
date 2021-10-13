import re  #RegEx Substituição

txt="Toradora - Taiga e Ryuji"

res=re.sub(" ","/",txt)

print(res)