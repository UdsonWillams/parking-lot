"""
Utilizamos um exemplo bem simples agora, mas imagine ter que desenvolver uma feature
de busca de alunos da Alura para que seja possível realizar a autenticação
no site ou app. Qual solução você usaria?
"""

# resolução https://www.alura.com.br/artigos/busca-binaria-aprenda-implementar-python"


import json
from time import time


def binary_search(data_list: list, searched_value: int) -> int | None:
    """
    Receive a list of ints and a searched value
    IF the value in the list return it, else return None.
    """
    low_value = 0
    high_value = len(data_list) - 1

    while low_value <= high_value:
        mid_Value = (low_value + high_value) // 2
        guess = data_list[mid_Value]
        if guess == searched_value:
            return mid_Value
        if guess > searched_value:
            high_value = mid_Value - 1
        else:
            low_value = mid_Value + 1
    return None


def normal_search(data_list: list, searched_value: int) -> int | None:
    index = 0
    for list_value in data_list:
        if list_value == searched_value:
            return index
        index += 1
    return None


if __name__ == "__main__":
    searched_value = 9536
    with open("items.json", "r") as file:
        data: dict = json.load(file)

    print("=" * 60)
    print(f"🔍 Buscando valor: {searched_value}\n")

    for idx, list_Value in enumerate(data.values(), 1):
        list_Value = sorted(list_Value)
        comparative_time = time()
        returned_value = binary_search(list_Value, searched_value)
        elapsed_time = time() - comparative_time
        # Mostra tempo em ms se < 1s, senão em segundos
        if elapsed_time < 1:
            tempo_fmt = f"{elapsed_time * 1000:.3f} ms"
        else:
            tempo_fmt = f"{elapsed_time:.3f} s"
        if returned_value is not None:
            print(f"[{idx}] Busca binária:")
            print(f"  Tempo decorrido: {tempo_fmt}")
            print(f"  ➜ Índice encontrado: {returned_value}")
            print(f"  ➜ Valor encontrado: {list_Value[returned_value]}")
            print("-" * 40)
    print("=" * 60)

    for idx, list_Value in enumerate(data.values(), 1):
        comparative_time = time()
        returned_value = normal_search(list_Value, searched_value)
        elapsed_time = time() - comparative_time
        if elapsed_time < 1:
            tempo_fmt = f"{elapsed_time * 1000:.3f} ms"
        else:
            tempo_fmt = f"{elapsed_time:.3f} s"
        if returned_value is not None:
            print(f"[{idx}] Busca linear:")
            print(f"  Tempo decorrido: {tempo_fmt}")
            print(f"  ➜ Índice encontrado: {returned_value}")
            print(f"  ➜ Valor encontrado: {list_Value[returned_value]}")
            print("-" * 40)
    print("=" * 60)
