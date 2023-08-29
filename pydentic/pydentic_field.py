from pydantic import (
    BaseModel,
    Field,
)


class UmTestePydenticField(BaseModel):
    status: str
    a_ser_testado: dict = Field(alias="a-ser-testado")


obj = {
    "status": "OK",
    "a-ser-testado": {
        "teste_1": "",
        "teste_2": "",
        "teste_3": "",
    },
}

teste_1 = UmTestePydenticField.parse_obj(obj)

print(teste_1)
teste_1.dict()
