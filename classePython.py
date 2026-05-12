#criação de classe em python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.") 
#criando um objeto da classe Pessoa
pessoa1 = Pessoa("André", 41)   
#usando o método apresentar do objeto pessoa1
pessoa1.apresentar()  # Output: Olá, meu nome é André e eu tenho 41 anos. 

#----------------------------------------------------------------------------------
# 1. Definição da Classe (O Molde)
class Carro:
    # Método Construtor (Inicializa os atributos)
    def __init__(self, marca, modelo):
        self.marca = marca   # Atributo
        self.modelo = modelo # Atributo

    # Método (Comportamento)
    def descrever(self):
        return f"Carro: {self.marca} {self.modelo}"

# 2. Criar Objeto (Instanciação)
# 'carro1' e 'carro2' são instâncias da classe Carro
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

# 3. Uso
print(carro1.descrever()) # Saída: Carro: Toyota Corolla
print(carro2.marca)       # Saída: Honda
