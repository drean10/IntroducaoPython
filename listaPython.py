#--------------------------------------------------------------------------------
#OBS : 
#lista = [1, 2, 3, 4, 5] pode mudar/adicionar/tirar elementos da lista.
#tuple = (1, 2, 3, 4, 5) não pode mudar os elementos da tupla depois de criada.
#set = {1, 2, 3, 4, 5} não pode conter elementos duplicados e não tem ordem específica.
#dict = {"key1": "value1", "key2": "value2"} é uma coleção de pares chave-valor, onde cada chave é única e mapeada para um valor.
#--------------------------------------------------------------------------------

#Trabalhando com listas 

nomes = ["Andre", "Maria", "João", "Ana"]
print(nomes) # Output: ['Andre', 'Maria', 'João', 'Ana']
print(nomes[0]) # Output: Andre
print(nomes[1]) # Output: Maria

#.append() para adicionar um elemento ao final da lista.
nomes.append("Carlos")
print(nomes) # Output: ['Andre', 'Maria', 'João', 'Ana', 'Carlos'] 

#.sort() para ordenar a lista em ordem alfabética.
nomes.sort()
print(nomes) # Output: ['Ana', 'Andre', 'Carlos', 'João', 'Maria']

#-------------------------------------------------------------------------------
quadrados = [ 1 , 4 , 9 , 16 , 25 ] + [ 30, 35, 40]
quadrados + [30,35,40] # [1, 4, 9, 16, 25, 30, 35, 40]
print ( quadrados )
print ( quadrados [ 0 ] ) # 1
print ( quadrados [ 4 ] ) # 25

#------------------------------------------------------------------------------

import math

infinity = float('inf')
not_a_number = float('nan')

print(infinity)     # inf
print(not_a_number) # nan

print(math.isinf(infinity))   # True
print(math.isnan(not_a_number)) # True

# Example 1: Basic concatenation
string1 = "Hello"
string2 = "World"
result = string1 + " " + string2  # Adding a space in between
print(result)  # Output: Hello World

#------------------------------------------------------------------------------
#Concatenação de strings
# Example 2: Concatenar variáveis ​​de diferentes tipos de dados (requer conversão de tipo)
name = "André"
age = 30
# TypeError: can only concatenate str (not "int") to str
# message = "My name is " + name + " and I am " + age # This will cause an error
message = "Meu nome é " + name + " Tenho " + str(age) + " anos." # Converte int em string
print(message)  # Output: Meu nome é André Tenho 30 anos.

# Outro tipo de concatenação usandoa a função join():
# Example: Usando join() com uma string vazia como separador
characters = ['P', 'y', 't', 'h', 'o', 'n']
word = "".join(characters)
print(word) # Output: Python

#------------------------------------------------------------------------------

# O += operador fornece uma maneira abreviada de adicionar elementos a uma string existente.
# Example: Acrescentar a uma string existente usando +=
greeting = "Hello"
greeting += " "  # Anexar um espaço
greeting += "there!" # Anexar "there!"
print(greeting)  # Output: Hello there!

#-------------------------------------------------------------------------------
#F-strings 

#F-strings (strings formatadas literais) - Formatação de strings

# Exemplo 1: Basico f-string formatting
name = "Andre"
age = 40
message = f"My name is {name} and I am {age} years old."
print(message)  # Output: Meu nome é Andre e tenho 40 anos de idade.

# Example 2: F-strings with expressions - Funçõ que faz igual ao f-string
x = 10
y = 5
result = f"The sum of {x} and {y} is {x + y}."
print(result)  # Output: The sum of 10 and 5 is 15.

# Example 3: F-strings with formatting specifications
pi = 3.14159265359
formatted_pi = f"The value of pi is approximately {pi:.2f}"  # Format to 2 decimal places
print(formatted_pi)  # Output: The value of pi is approximately 3.14

#-------------------------------------------------------------------------------
#.format() - Método de formatação de strings

# Example 1: Formatação básica com .format()
name = "Andre"
age = 40
message = "My name is {} and I am {} years old.".format(name, age)
print(message)  # Output: My name is Andre and I am 40 years old.

# Example 2: Formatting with positional arguments
message = "Meu nome é {1} e tenho {0} anos de idade.".format(age, name)
print(message)  # Output: Meu nome é Andre e tenho 40 anos de idade.

# Example 3: Formatting with keyword arguments
message = "Meu nome é {name} e tenho {age} anos de idade.".format(name="Andre", age=40)
print(message)  # Output: Meu nome é Andre e tenho 40 anos de idade.



