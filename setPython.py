#se adicionar um elemento a um conjunto, use o método add()
#se adicionar vários elementos a um conjunto, use o método update()
#se remover um elemento de um conjunto, use o método remove() ou discard()
#se verificar se um elemento está presente em um conjunto, use o operador in
#se obter a quantidade de elementos em um conjunto, use a função len()
#exemplo de uso de conjuntos em Python, não repete elementos e não mantém ordem

s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(4 - 2)  # Este elemento é igual a 2, então não será adicionado novamente
s.add(2)      # Este elemento não será adicionado novamente
print(s)  # Output: {1, 2, 3, 4}

#.remove() lança um erro se o elemento não estiver presente, enquanto .discard() não faz nada
s.remove(1)  # Remove o elemento 1 do conjunto 
print(s)  # Output: {2}

#len() retorna o número de elementos únicos no conjunto
print(f"A quantidade de {len(s)} elementos.")  # Output: 1

s.discard(3)  # Remove o elemento 3 do conjunto     
print(s)  # Output: {2}
