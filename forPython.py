# Exemplo de duas formas de importar a função quadrado do arquivo funcaoPython.py e 
# usá-la para calcular o quadrado dos números de 0 a 9 usando um loop for.

from funcaoPython import *

for i in range(10):
    print(f"O quadrado de {i} é {quadrado(i)}")
    

#outra forma de inportar a função quadrado do arquivo funcaoPython.py
import funcaoPython

for i in range(10):
    print(f"O quadrado de {i} é {funcaoPython.quadrado(i)}")