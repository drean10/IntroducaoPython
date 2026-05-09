#for e while são estruturas de controle de fluxo que permitem executar um bloco de código repetidamente com base em uma condição.
#Uando break e continue para controlar o fluxo de loops em Python
#------------------------------------------------------------------------------

# Example: Prompting the user for input until they enter "quit"
user_input = ""
while user_input != "sair":
    user_input = input("Digite um comando (ou 'sair' para sair): ")
    print(f"Você digitou: {user_input}")

#-----------------------------------------------------------------------------
#As instruções ` breakif` e `else` continuesão ferramentas poderosas para controlar o fluxo de loops em Python

# Example: Procurar um número específico em uma lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alvo = 5

for numero in numeros:
    print(f"Checando número: {numero}")
    if numero == alvo:
        print(f"Encontrou o alvo: {alvo}")
        break  # Saia do loop quando o alvo for encontrado.
    else:
        print(f"{numero} não é o alvo.")

print("Loop finished.") 

#-----------------------------------------------------------------------

# Example: Breaking out of an inner loop
for i in range(3):
    print(f"Iteração do loop externo: {i}")
    for j in range(5):
        print(f"  Iteração do loop interno: {j}")
        if j == 2:
            print("  Saindo do loop interno")
            break  # Breaks only the inner loop
    print("Outer loop continues")
print("Program finished.")

#-----------------------------------------------------------------------------

# Example: Breaking a while loop
count = 0
while True:  # Infinite loop
    print(f"Count: {count}")
    count += 1
    if count > 5:
        print("Breaking out of the while loop")
        break  # Exit the loop when count is greater than 5

print("Loop finished.")

#-----------------------------------------------------------------------------

# Exemplo: continue para pular uma iteração específica
# Example: Printing only odd numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:  # Check if the number is even
        continue  # Skip the rest of the iteration if the number is even
    print(f"Odd number: {number}")

print("Loop finished.")


#------------------------------------------------------------------------------

# Example: Using continue in nested loops
for i in range(3):
    print(f"Iteração do loop externo: {i}")
    for j in range(5):
        if j == 2:
            print(" Ignorando a iteração do loop interno 2")
            continue  # Ignora o restante da iteração do loop interno.
        print(f"  Iteração do loop interno: {j}")
    print("O loop externo continua")

print("Program finished.")


#------------------------------------------------------------------------------

# Example: Using continue in a while loop
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        print(f"Skipping even number: {count}")
        continue  # Skip even numbers
    print(f"Odd number: {count}")

print("Loop finished.")

#------------------------------------------------------------------------------

# Example: Validating user input
while True:
    user_input = input("Enter a number (or 'q' to quit): ")

    if user_input.lower() == 'q':
        break  # Exit the loop if the user enters 'q'

    try:
        number = float(user_input)  # Convert the input to a float
        print(f"You entered: {number}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue  # Skip to the next iteration if the input is not a number

"""Neste exemplo:

O while Trueloop continua até que o usuário digite 'q'.
O try-exceptbloco tenta converter a entrada do usuário em um número de ponto flutuante.
Se a conversão falhar (ou seja, se a entrada não for um número válido), uma ValueErrorexceção é lançada e a continueinstrução passa para a próxima iteração, solicitando novamente a entrada do usuário.
Se a entrada for um número válido, ele será impresso."""

#-------------------------------------------------------------------------------

#numero primo é um número inteiro maior que 1 que não tem divisores positivos além de 1 e ele mesmo.

def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for number in range(2, 20):  # Check numbers from 2 to 19
    if is_prime(number):
        print(f"The first prime number found is: {number}")
        break  # Exit the loop after finding the first prime number