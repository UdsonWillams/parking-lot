from typing import (
    List,
    Optional,
)

from pydantic import BaseModel

# Documentação que fala mais sobre
# https://docs.pydantic.dev/usage/models/


class Bebida(BaseModel):
    id: int
    name: str  # Optional depois do python-10 foi abolido e utilizamos > |
    description: Optional[str] = None


class Fruta(BaseModel):
    maca: bool
    banana = "banana"


class Carrinho(BaseModel):
    fruta: Fruta
    bebidas: List[Bebida]


carrinho_1 = Carrinho(
    fruta={"maca": True},
    bebidas=[{"id": "1", "name": "jack daniels", "description": "whiskey muito bom"}],
)
# outra forma de fazer isso é com o parse_obj
# carrinho = {"fruta": {"maca": True}, "bebidas": \
# [{"id": "1", "name": "jack daniels", "description": "whiskey muito bom"}]}
# carrinho_1 = Carrinho.parse_obj(carrinho)

print(carrinho_1)
assert type(carrinho_1.bebidas) == list
assert carrinho_1.fruta.maca is True
