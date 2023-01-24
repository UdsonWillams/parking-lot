from pydantic import BaseModel

#classe basica do pydentic, se importa a classe BaseModel
class User(BaseModel):
    id: int
    name = "Udson Willams"

#caso não seja passado que o parametro é opcional, o objeto não é instanciavel
# user = User()
# também é necessario mandar os valores com o mesmo tipo que foram instanciados
# id não pode ser str por exemplo

user_1 = User(id=1)
# alguns metodos legais ja trazidos pelo BaseModel são os
# dict, json, parse_object
print(user_1.dict())  # trás o objeto como dicionario. 
print(user_1.json())    # trás o objeto como json. 
# O Parse object faz a classe User conseguir instanciar um objeto a partir de um dicionario.
# ex.:.
new_user = {"id": 2, "name": "joaozinho"}
user_2 = User.parse_obj(new_user)

assert user_1.id == 1
assert user_1.name == "Udson Willams"
assert user_2.id == 2
assert user_2.name == "joaozinho"

#  também é possivel criar um JSON schema de validação a partir do objeto criado
# print(user_1.schema())
# print(user_1.schema_json())

# cria um modelo sem validação, oque é perigoso mas pode ser util alguma hora.
user_without_validation = User.construct(number="2")
print(user_without_validation.number)
# print(user_without_validation.id) retorna um erro por que o valor nunca foi instanciado.
