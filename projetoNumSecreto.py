import random

lower_bound = 1
upper_bound = 100
secret_number = random.randint(lower_bound, upper_bound)

print(f"Estou pensando em um número entre {lower_bound} e {upper_bound}.")

guess_count = 0 # Initialize the guess counter

while True:
    try:
        guess = int(input("Dê um palpite: "))
        guess_count += 1 # Increment the guess counter
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        continue # Go to the next iteration of the loop

    if guess < secret_number:
        print("Muito baixo!")
    elif guess > secret_number:
        print("Muito alto!")
    else:
        print(f"Parabéns! Você acertou o número em {guess_count} tentativas!")
        break # Exit the loop when the guess is correct