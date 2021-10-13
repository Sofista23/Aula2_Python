import json

carrosDictionary={
    "Marca":"Honda",
    "Modelo":"HRV",
    "Cor":"Prata"
    }

carrosJson=json.dumps(carrosDictionary,indent=4,separators=(":","="))

print(carrosJson)