def retorno(valor: bool):
    return valor


# verifica se o valor da expressão passada é true,
# e se for True instancia A com oque for retornado na expressão.
if a := retorno(True):
    print(a) if a is True else print("A is False")
assert a is True

if a := retorno(False):
    print("não serei printado, pois o retorno foi false.")
assert a is False
