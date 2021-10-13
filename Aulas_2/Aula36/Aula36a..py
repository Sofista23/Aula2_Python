#Converter de JSON para DICTIONARY  
import json

carrosJson='{"Marca":"Honda","Modelo":"HRV","Cor":"Prata"}'

carros=json.loads(carrosJson)

print(carros)

for x,y in carros.items():
    print(f"{x}: {y}")