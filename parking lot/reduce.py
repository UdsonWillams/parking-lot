# a função reduce, meio que roda uma função
# encima de um interador.

# Nesse exemplo usamos a função getitem
# passamos ao reduce a função que vai "rodar"
# e path e data vão ser "interadas", nesse exmplo é o mesmo de fazer
# data.get("argentina").get("pais")
import operator
from functools import reduce

path = ["teste_1", "pais"]
data = {
    "teste_1": {
        "pais": "ARGENTINA - UPPER",
        "criação": "",
        "valor": "",
    },
    "teste_2": {
        "pais": "BRASIL - UPPER",
        "criação": "",
        "valor": "",
    },
}
teste = reduce(operator.getitem, path, data)
print(teste)
