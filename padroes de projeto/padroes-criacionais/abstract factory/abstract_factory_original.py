from __future__ import annotations

from abc import (
    ABC,
    abstractmethod,
)


class AbstractFactory(ABC):
    """
    A interface da fabrica declara um conjunto de funções que retorna
    diferentes tipos de produtos abstratos.

    Esses produtos são chamados de familia e são mais conceitos
    relacionados aos tipos de produtos que poderemos reproduzir.
    """

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        """
        Cria produtos do tipo A
        """
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        """
        Cria produtos do tipo B
        """
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Uma fabrica "concreta" produz produtos de uma unica variante

    As funções de criação são anotadas para retornar um produto
    abstrato, mas o retorno real é produto concreto.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Cada fabrica de produto concreto, possui uma variante
    do produto especifico.

    Ex.: Na fabrica acima, retornamos um produtoA1 e nessa um A2
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


class AbstractProductA(ABC):
    """
    Cada produto dinstinto deve implementar sua propria interface

    E cada variante desse produto deve "implementar" essa interface.
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


class ConcreteProductA1(AbstractProductA):
    """
    Os produtos concretos são criados pela fabrica
    concreta correspondente.
    """

    def useful_function_a(self) -> str:
        return "Retornando um produto A1."


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "Retornando um produto A2."


class AbstractProductB(ABC):
    """
    Interface base de outro produto. todos que herdarem daqui
    podem interagir entre si, mas a melhor interação é entre
    produtos da mesma variante concreta.
    """

    @abstractmethod
    def useful_function_b(self) -> None:
        r"""
        O produto B é capaz de fazer suas próprias coisas... \/\/
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """
        ... Mas também pode colaborar com os Produtos A
        A Abstract Factory garante que todos os produtos
        que cria sejam da mesma variante e, portanto, compatíveis.
        """
        pass


class ConcreteProductB1(AbstractProductB):
    """
    Essa variante, Produto B1 só consegue funcionar corretamente com a
    variante de produto A1, porém aceita qualquer instancia de produtos
    AbstractProductA como argumento.
    """

    def useful_function_b(self) -> str:
        return "O retorno de um produto B1."

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"O resultado de B1 colaborando com \N{rightwards arrow} {result}"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "O retorno de um produto B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        """
        Essa variante, Produto B2 só consegue funcionar corretamente com a
        variante de produto A2, porém aceita qualquer instancia de produtos
        AbstractProductA como argumento.
        """
        result = collaborator.useful_function_a()
        return f"O resultado de B2 colaborando com \N{rightwards arrow}  {result}"


def client_code(factory: AbstractFactory) -> None:
    """
    Essa função vai funcionar com fábricas e produtos de tipos abstratos:
    AbstractFactory e AbstractProduct.

    Isso permite passar qualquer subclasse de fábrica ou produto
    para o código do cliente sem quebrá-lo.
    """
    product_a = factory.create_product_a()  # cria produto A
    product_b = factory.create_product_b()  # cria produto B

    print(f"{product_b.useful_function_b()}")  # produto b
    print(
        f"{product_b.another_useful_function_b(product_a)}", end=""
    )  # produto b junto de produto a


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("\n")
    print("Testando codigo com a primeira fabrica: ")
    client_code(ConcreteFactory1())
    print("\n")
    print("Testando codigo com a segunda fabrica: ")
    client_code(ConcreteFactory2())
    print("\n")
