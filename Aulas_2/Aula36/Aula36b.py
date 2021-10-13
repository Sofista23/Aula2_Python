#Converter de DICTIONARY para JSON  
import json

carros={
    "Marca":"Honda",
    "Modelo":"HRV",
    "Cor":"Prata"
    }

carrosJson=json.dumps(carros)

print(carrosJson)

