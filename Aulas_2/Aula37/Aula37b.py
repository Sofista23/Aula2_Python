import json

pessoa={
    "nome":"Taiga",
    "Time":"Meninas",
    "Vivo":"True",
    "Energina":100,
    "Mochila":["Corda","Tigre"],
    "Amigos":[
        {"Nome":"Ryuuji","Procimidade":"Alta"},
        {"Nome":"Minori","Procimidade":"Muito Alta"},
        {"Nome":"Kitamura","Procimidade":"Média"}
    ]
}

pessoaJson=json.dumps(pessoa,indent=3)

print(pessoaJson)

print("-="*45)

print(pessoa["Mochila"])