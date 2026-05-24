
#Um decorador é uma função que recebe outra função como argumento e retorna uma nova função que geralmente 
# estende o comportamento da função original sem modificá-la diretamente.

def anunciar(f):
    def nova_funcao():
        print("Anúncio: A função está prestes a ser executada.")
        f()
        print("Anúncio: A função foi executada.")
    return nova_funcao 

@anunciar
def minha_funcao():
    print("@anunciar:Esta é a função original.")
minha_funcao()