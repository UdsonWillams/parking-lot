import secrets
import string

alphabet = string.ascii_letters + string.digits + "!@#()"
password = "".join(secrets.choice(alphabet) for i in range(20))

print(password)
# outra forma
# code = "".join(random.choice(string.digits) for _ in range(6))
