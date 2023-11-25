from __future__ import annotations

from abc import (
    ABC,
    abstractmethod,
)

# O padrão Builder Não é muito usual no python
# Então achei melhor so falar sobre ele, e mostrar o jeito pythonico
# E não mostrar implementação "original"


class CarBuilder(ABC):
    """
    A interface do CarBuilder especifica métodos para criar
    as diferentes partes dos objetos Produto.
    """

    @abstractmethod
    def __init__(self, marca, cor, ano) -> None:
        self.marca = marca
        self.cor = cor
        self.ano = ano
        super().__init__()


class ConcreteCar(CarBuilder):
    def __init__(self, marca="", cor="", ano="") -> None:
        self.marca = marca
        self.cor = cor
        self.ano = ano

    def __str__(self) -> str:
        car_str = (
            f"Carro de marca: {self.marca} - "
            f"De cor: {self.cor} - "
            f"De ano: {self.ano}"
        )

        return car_str


car_1 = ConcreteCar(marca="wolks", cor="preto", ano=2020)
car_2 = ConcreteCar(marca="wolks", cor="preto")

if __name__ == "__main__":
    print("\n")
    # Carro totalmente montado
    print(car_1)
    # Carro parcialmente montado
    print(car_2)
    print("\n")
