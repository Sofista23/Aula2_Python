#Key:Value
carros={
    "Fabricante":"Honda",
    "Modelo":"HRV",
    "Ano":"2021"
}
carros["Cambio"]="Autmático"
carros.pop("Cambio")

fab=carros.get("Fabricante")
mod=carros["Modelo"]

print(fab)
print(mod)
print(carros["Ano"])

print("-="*35)

for x in carros:
    print(x+": "+carros[x])

print("-="*35)

print(f"Tamanho do DICTIONARY: {len(carros)}")