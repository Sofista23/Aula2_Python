import re  #RegEx Mostra o local que encontrou

txt="Toradora - Taiga e Ryuji"

res=re.search("Taiga",txt)

print(f"String de Inicio: {res.start()} / String do Final: {res.end()}")