from pydantic import BaseModel, ValidationError, validator

"""
Mais sobre validadores
https://docs.pydantic.dev/usage/validators/
"""


class User(BaseModel):
    id: int
    name: str

    @validator(
        "name"
    )  # faz uma validação de campos, parecido com o validate_campo do drf
    def value_must_equal_udson(cls, v):
        """
        É bom que se pode por logica num campo aonde se queira validar, e deixa o codigo
        mais fácil de saber que a validação funcionou
        """
        if v != "Udson":
            raise ValueError("value must be 'Udson'")
        return v


try:
    User(id=1, name="ber")
except ValidationError as e:
    errors = e.errors()
    """
    O retorno será
    [
        {
            'loc': ('name',),
            'msg': 'value must be "Udson"',
            'type': 'value_error'
        }
    ]
    """

assert errors[0].get("msg") == "value must be 'Udson'"
