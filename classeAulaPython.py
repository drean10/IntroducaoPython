class Voo:
    def __init__(self, capacidade: int):
        self.capacidade = capacidade
        self.passageiros: list[str] = []

    def assentos_disponiveis(self) -> int:
        """Retorna quantos assentos ainda estão livres."""
        return self.capacidade - len(self.passageiros)

    def open_seats(self) -> bool:
        """Retorna True se ainda houver assentos disponíveis."""
        return self.assentos_disponiveis() > 0

    def add_passageiros(self, nome: str) -> bool:
        if not self.open_seats():
            return False

        self.passageiros.append(nome)  # adiciona o nome do passageiro à lista
        return True


# Instancia e usa a classe
voo = Voo(4)

pessoas = ["André","Alice", "Bob", "Charlie", "David"]
for pessoa in pessoas:
    if voo.add_passageiros(pessoa):
        print(f"{pessoa} foi adicionado com sucesso.")
    else:
        print(f"Desculpe, não há assentos disponíveis para {pessoa}.")

