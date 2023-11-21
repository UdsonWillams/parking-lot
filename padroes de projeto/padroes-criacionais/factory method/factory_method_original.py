from __future__ import annotations

from abc import (
    ABC,
    abstractmethod,
)


class CreatorInterface(ABC):  # interface de criação!
    """
    Essa "interface" declara a função de fábricação que deve retornar
    um objeto de uma classe Produto. As subclasses do Creator
    geralmente fornecem a implementação desta função.
    """

    @abstractmethod
    def factory_method(self):
        """
        A interface pode fornecer alguma implementação padrão do método de fábricação.
        """
        pass

    def return_product_name(self) -> str:
        """
        Apesar do nome a resposabilidade do criador não é criar os produtos, ela pode
        conter logicas que são usadas nas classes "PRODUTO"

        As subclasses podem sobrescrever essas logicas e retornarem valores diferentes
        do que o metodo "original".
        """

        # chamada do metodo factory_method para criar um objeto do tipo Produto
        product = self.factory_method()

        # Agora conseguimos usar o produto.
        result = (
            f"CreatorInterface: O nome da classe do produto é: {product.return_name()}"
        )
        return result


class Product(ABC):  # Podia ser produto, carro, bici, Error, etc :)
    """
    A interface Produto declara as operações que todos os produtos concretos
    devem implementar
    """

    @abstractmethod
    def operation(self) -> str:
        pass


# Criadores concretos sobrescrevem o metodo
# factory_method para poder mudar seus retornos.


class ConcreteCreator1(CreatorInterface):
    """
    Observe que o type hint do método ainda retorna o tipo de produto abstrato,
    mesmo que o produto real seja retornado do método. Desta forma, o Criador
    pode permanecer independente de classes concretas de produtos.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(CreatorInterface):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


# Concrete Products provide various implementations of the Product interface.


class ConcreteProduct1(Product):
    def __init__(self) -> None:
        self.name = "ConcreteProduct1"
        super().__init__()

    def operation(self) -> str:  # redefine sua função operation
        return "{Retorno da classe ConcreteProduct1}"

    def return_name(self) -> str:
        return self.name


class ConcreteProduct2(Product):
    def __init__(self) -> None:
        self.name = "ConcreteProduct2"
        super().__init__()

    def operation(self) -> str:  # redefine sua função operation
        return "{Retorno da classe ConcreteProduct2}"

    def return_name(self) -> str:
        return self.name


# Cada classe retornou seu proprio metodo como precisava.


def client_code(creator: CreatorInterface) -> None:
    """
    Essa função funciona com uma instância de um criador concreto.

    Contanto que a função receba um criador que herde da interface base
    Ela vai conseguir chamar o metodo que criamos e no caso manejar o objeto Produto.
    """

    print(
        f"Client: Não conheço a classe do criador, mas ainda funciono xD\n"
        f"{creator.return_product_name()}",
        end="",
    )


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
