carros = [
    {"marca": "Ford", "ano": 2020},
    {"marca": "Toyota", "ano": 2018},
    {"marca": "Honda", "ano": 2021},
    {"marca": "Ford", "ano": 2019},
    {"marca": "Toyota", "ano": 2022},
    {"marca": "Honda", "ano": 2019},
]

def ordenar_carros(carros):
    return sorted(
        carros,
        key=lambda c: (c["marca"], c["ano"])  
    )

carros_ordenados = ordenar_carros(carros)

for carro in carros_ordenados:
    print(f'Marca: {carro["marca"]}, Ano: {carro["ano"]}')
