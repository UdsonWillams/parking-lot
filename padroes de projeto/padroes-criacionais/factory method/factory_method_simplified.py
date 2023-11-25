from __future__ import annotations

from abc import (
    ABC,
    abstractmethod,
)


class Product(ABC):  # Podia ser produto, carro, bici, Error, etc :)
    """
    A interface Produto declara as operações que todos os produtos concretos
    devem implementar
    """

    @abstractmethod
    def operation(self) -> str:
        pass

    def return_product_name(self) -> str:
        """
        Apesar do nome a resposabilidade do criador não é criar os produtos, ela pode
        conter logicas que são usadas nas classes "PRODUTO"

        As subclasses podem sobrescrever essas logicas e retornarem valores diferentes
        do que o metodo "original".
        """

        # Agora conseguimos usar o produto.
        result = f"ProductInterface: O nome da classe do produto é: {self.name}"
        return result


class ConcreteProduct1(Product):
    """
    Concrete Products provide various implementations of the Product interface.
    """

    def __init__(self, name="ConcreteProduct1") -> None:
        self.name = name

    def operation(self) -> str:  # redefine sua função operation
        return "{Retorno da classe ConcreteProduct1}"


class ConcreteProduct2(Product):
    def __init__(self, name="ConcreteProduct2") -> None:
        self.name = name

    def operation(self) -> str:  # redefine sua função operation
        return "{Retorno da classe ConcreteProduct2}"

    def return_product_name(self) -> str:
        """
        Retorno o nome do produto direto!
        """

        # Agora conseguimos usar o produto.
        result = "Não passei na ProductInterface: O "
        f"nome da classe do produto é: {self.name}"
        return result


def client_code(creator: Product) -> None:
    """
    Essa função funciona com uma instância de um criador concreto.

    Contanto que a função receba um criador que herde da interface base
    Ela vai conseguir chamar o metodo que criamos e no caso manejar o objeto Produto.
    """

    print(
        f"{creator.return_product_name()}",
        end="",
    )


if __name__ == "__main__":
    print("App: feito com o produto: ConcreteProduct1.")
    client_code(ConcreteProduct1())
    print("\n")

    print("App: feito com o produto: ConcreteProduct2.")
    client_code(ConcreteProduct2())
    print("\n")
