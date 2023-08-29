from pydantic import (
    BaseModel,
    validator,
)


class UserModel(BaseModel):
    """
    Como utilizar validações no fastapi de forma fácil
    passa um decorator com o valor no atributo dentro
    cria uma funcção que faz algum tipo de validação,
    retornando erro caso não seja o valor que foi requerido.
    """

    name: str
    username: str
    password1: str
    password2: str

    @validator("name")
    def name_must_contain_space(cls, v):
        if " " not in v:
            raise ValueError("must contain a space")
        return v.title()

    @validator("password2")
    def passwords_match(cls, v, values, **kwargs):
        print(kwargs)
        if "password1" in values and v != values["password1"]:
            raise ValueError("passwords do not match")
        return v

    @validator("username")
    def username_alphanumeric(cls, v):
        assert v.isalnum(), "must be alphanumeric"
        return v


user = UserModel(
    name="samuel colvin",
    username="scolvin",
    password1="zxcvbn",
    password2="zxcvbn",
)
print(user)
