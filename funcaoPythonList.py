nomes = [
    {"nome": "Andre", "cidade": "itaberaí"},
    {"nome": "joao", "cidade": "sao paulo"},
    {"nome": "maria", "cidade": "salvador"} 
]
"""def imprimir_nomes(pessoa):
    return pessoa["cidade"]"""

nomes.sort(key=lambda pessoa: pessoa["nome"])
print(nomes)
