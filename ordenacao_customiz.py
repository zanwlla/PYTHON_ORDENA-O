carros = [
    {"marca": "Ford", "ano": 2020},
    {"marca": "Toyota", "ano": 2023},
    {"marca": "Honda", "ano": 2011},
    {"marca": "Ford", "ano": 2019},
    {"marca": "Toyota", "ano": 2024},
    {"marca": "Honda", "ano": 2005},
]

def custom_order(marca):
    prioridade = 0 if marca.startswith('T') else 1
    return (prioridade, marca)

def ordenar_carros_customizados(carros):
    return sorted(
        carros,
        key=lambda c: (custom_order(c["marca"]), -c["ano"])  
    )

carros_ordenados = ordenar_carros_customizados(carros)

for carro in carros_ordenados:
    print(f'Marca: {carro["marca"]}, Ano: {carro["ano"]}')
