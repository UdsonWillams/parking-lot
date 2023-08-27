"""
Utilizamos um exemplo bem simples agora, mas imagine ter que desenvolver uma feature
de busca de alunos da Alura para que seja possível realizar a autenticação
no site ou app. Qual solução você usaria?
"""
# resolução https://www.alura.com.br/artigos/busca-binaria-aprenda-implementar-python"


from time import time

import json


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
            return  index
        index += 1
    return None
 

if __name__ == "__main__":
    searched_value = 2496
    with open("01_introduction_to_algorithms/items.json", "r") as file:
        data: dict = json.load(file)

    print(50 * "=")
    for list_Value in data.values():
        comparative_time = time()
        returned_value = binary_search(list_Value, searched_value)
        elapsed_time = time() - comparative_time
        print(f"Elapsed time: {elapsed_time}")
        if returned_value:
            print(f"The return of the search is: {returned_value} - This is the index value.")
            print(f"Searched value: {searched_value} | Finded value: {list_Value[returned_value]}" + "\n" + 40 * "-")
        else:
            print("The value is not finded" + "\n" + 40 * "-")
    print(50 * "=")
    returned_value = None
    for list_Value in data.values():
        comparative_time = time()
        returned_value = normal_search(list_Value, searched_value)
        elapsed_time = time() - comparative_time
        print(f"Elapsed time: {elapsed_time}")
        if returned_value:
            print(f"The return of the search is: {returned_value} - This is the index value.")
            print(f"Searched value: {searched_value} | Finded value: {list_Value[returned_value]}" + "\n" + 40 * "-")
        else:
            print("The value is not finded" + "\n" + 40 * "-")
    print(50 * "=")
