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