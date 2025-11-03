import json

dados = {
    "livros": [
        {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
        {"titulo": "O Guarani", "autor": "José de Alencar", "ano": 1857},
        {"titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis", "ano": 1881},
        {"titulo": "Iracema", "autor": "José de Alencar", "ano": 1865},
        {"titulo": "A Moreninha", "autor": "Joaquim Manuel de Macedo", "ano": 1844}
    ]
}

with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)  # Escreve o dicionário em um arquivo JSON com indentação de 4 espaços

