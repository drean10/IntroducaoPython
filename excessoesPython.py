import sys
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Erro: Valor inválido. Certifique-se de digitar um número inteiro.")
    sys.exit(0)

try:
    resultado = x/y
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
    sys.exit(0)

print(f"{x} / {y} = {resultado}")