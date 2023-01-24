from typing import List
from pydantic import BaseModel, ValidationError, conint


class Location(BaseModel):
    lat = 0.1
    lng = 10.1


class Model(BaseModel):
    is_required: float
    gt_int: conint(gt=42)
    list_of_ints: List[int] = None
    a_float: float = None
    recursive_model: Location = None


data = dict(
    list_of_ints=['1', 2, 'bad'],
    a_float='not a float',
    recursive_model={'lat': 4.2, 'lng': 'New York'},
    gt_int=21,
)

try:
    Model(**data) # em caso de erro de validação de tipo, retorna o campo e o tipo que ele espera
except ValidationError as e:
    e.errors() # quantos erros retornaram na inicialização
    print(e)

try:
    Model(**data) # em caso de erro de validação de tipo, retorna mais dados em formato json
except ValidationError as e:
    print(e.json())
