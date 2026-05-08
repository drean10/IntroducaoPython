age = 20

if age >= 18:
    print("Você tem direito a votar.")  # This line will be executed because age is 20

    #-------------------------------------------------------------------------------

x = 10
y = 5
if x > y:
    print("x é maior que y")  # x é mair que y
if x != y:
    print("x não é igual a y")  # x não é igual a y
if x == y:
    print("x é igual a y")  # Esta linha NÃO será executada.

#-------------------------------------------------------------------------------

age = 25

if age > 18:
    print("You are an adult.")
    print("You can drive.")  # Ambas as linhas fazem parte do bloco 'if'.

#-------------------------------------------------------------------------------

temperature = 75

if temperature > 80:
    print("It's hot!")
elif temperature > 60:
   print("It's warm.")  # Output: It's warm.
elif temperature > 40:
    print("It's mild.")
else:
    print("It's cold.")

x = 10
y = 5

if x > 0:
    print("x is positive.")  # Output: x is positive.
    if y > 0:
        print("y is also positive.")  # Output: y is also positive.
    else:
        print("y is not positive.")
else:
    print("x is not positive.")

#--------------------------------------------------------------------------------

username = input("Digite seu nome de usuário: ")
if username == "":
    print("O nome de usuário não pode estar vazio.")
else:
    print("O nome de usuário é válido.")

password = input("Digite sua senha: ")
if len(password) < 8:
    print("A senha deve ter pelo menos 8 caracteres.")
else:
    print("A senha é válida.")

#-------------------------------------------------------------------------------
# Usando For para iterar sobre uma lista de frutas

# Example: Iterating through a list of fruits
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


#Utilizando a range()função para criar uma sequência de números
# Example: Usando a função range() para imprimir números de 0 a 4.
for i in range(5):
    print(i)


# Example: Usando a função range() para imprimir números de 2 a 5.
for i in range(2, 6):
    print(i)

# Example: Usando a função range() para imprimir números pares de 0 a 10
for i in range(0, 11, 2):
    print(i)

#forLaços Aninhados
# Example: 
# Laços for aninhados para imprimir coordenadas
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")