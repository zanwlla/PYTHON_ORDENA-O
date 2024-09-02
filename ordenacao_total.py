carros = [
    {"marca": "Ford", "ano": 2020, "modelo": "Focus"},
    {"marca": "Toyota", "ano": 2018, "modelo": "Corolla"},
    {"marca": "Honda", "ano": 2021, "modelo": "Civic"},
    {"marca": "Ford", "ano": 2019, "modelo": "Fiesta"},
    {"marca": "Toyota", "ano": 2022, "modelo": "Camry"},
    {"marca": "Honda", "ano": 2019, "modelo": "Accord"},
    {"marca": "Toyota", "ano": 2020, "modelo": "Yaris"},
]

def ordenar_total(carros):
    return sorted(
        carros,
        key=lambda c: (c["marca"], c["ano"], c["modelo"]) 
    )

carros_ordenados = ordenar_total(carros)

for carro in carros_ordenados:
    print(f'Marca: {carro["marca"]}, Ano: {carro["ano"]}, Modelo: {carro["modelo"]}')
