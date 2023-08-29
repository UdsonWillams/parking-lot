# Sempre bom olhar os valores que o metodo recebe.
# Ao passar uma tupla. ele verifica se a string passada
# bate com o padrão passado na tupla.

path = "/api/v1/users/212313213/"
print(path.startswith(("/api/v1/users/", "/teste/da_silva/info/")))

path = "/teste/da_silva/3213123"
print(path.startswith(("/api/v1/users/", "/teste/da_silva/3213123")))
