# A ideia é poder passar os valores de entrada e
# saida, e o script responder a correta de sair do job.
# com base que o horario são 8 horas diarias.

# TODO
from datetime import datetime

entrada1 = datetime.strptime("08-45", "%H-%M")
saida1 = datetime.strptime("14-14", "%H-%M")

entrada2 = datetime.strptime("14-50", "%H-%M")

final = saida1 - entrada1


cont_hr = 0
cont_min = 0
while final.days < 8:
    if cont_min > 60:
        cont_min = 0
        cont_hr += 1
    saida = datetime.strptime(f"{cont_hr}-{cont_min}", "%H-%M")
    entrada2 + saida
    final = final + saida1

print(final)
