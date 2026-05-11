#dicionario em palavras simples é uma coleção de itens onde cada item tem uma chave e um valor.
#Dicionário é uma estrutura de dados que armazena pares de chave-valor.
#Criando um dicionário
pessoa = {
    "nome": "Alice",
    "idade": 30,
    "cidade": "São Paulo"
}
#Acessando valores em um dicionário
print(pessoa["nome"])  # Output: Alice  
print(pessoa["idade"])  # Output: 30
print(pessoa["cidade"])  # Output: São Paulo 
#Adicionando ou atualizando itens em um dicionário
pessoa["profissão"] = "Engenheira"  # Adiciona um novo item
pessoa["idade"] = 31  # Atualiza o valor da chave "idade"
print(pessoa)  # Output: {'nome': 'Alice', 'idade': 31, 'cidade': 'São Paulo', 'profissão': 'Engenheira'}