# script que verifica a idade.
from datetime import (
    datetime,
    timezone,
)

nascimento = "2000-04-16"
nascimento_datetime = datetime.strptime(nascimento, "%Y-%m-%d")

# se ligar nesse timezone.utc
hoje = datetime.now(timezone.utc)

a = (hoje.month, hoje.day) < (nascimento_datetime.month, nascimento_datetime.day)
idade = hoje.year - nascimento_datetime.year - (a)
print(f"Hoje | dia: {hoje.day} | mes: {hoje.month}")
print(
    f"Seu nascimento | dia: {nascimento_datetime.day} |"
    f"mes: {nascimento_datetime.month}"
)

print(f"Sua idade é: {idade}")
