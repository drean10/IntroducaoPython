# Acessando caracteres de uma string
palavra = 'Python'
palavra [ 0 ] # caractere na posição 0 'P' 
palavra [ 5 ] # caractere na posição 5 ' n ' 
palavra [ -5 ] # caractere na posição -5 'y'
palavra [ 2 : 5 ] # caracteres da posição 2 (incluído) à 5 (excluído) 'tho'
palavra = 'J'  + palavra [ 1 : ]
print ( palavra [ 0 ] )
print ( palavra [ 5 ] )
print ( palavra [ -5 ] )
print ( palavra [ 2 : 5 ] )

var = 3  *  'un'  +  'ium'  "\n" 'Py'  'thon' 
print ( var ) # 'unununium'

palavra = 'Python'
var = 'J'  + palavra [ 1 : ]
print ( var ) # 'Jython'

palavra[ : 2 ]  +  'py' 
print ( palavra) # 'Pypthon'

s =  'supercalifragilisticexpialidocious' 
print ( len ( s ) ) # 34


#lista = [1, 2, 3, 4, 5] pode mudar/adicionar/tirar elementos da lista.
#tuple = (1, 2, 3, 4, 5) não pode mudar os elementos da tupla depois de criada.
#set = {1, 2, 3, 4, 5} não pode conter elementos duplicados e não tem ordem específica.
#dict = {"key1": "value1", "key2": "value2"} é uma coleção de pares chave-valor, onde cada chave é única e mapeada para um valor.