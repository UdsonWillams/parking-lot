# shebang \/\/ ver mais sobre shebang here: https://realpython.com/python-shebang/
# !/usr/bin/python3

# adicionar o -m nos comandos python roda o codigo do pacote __main__.py
from time import sleep

print("This is my file to test Python's execution methods.")
print("The variable __name__ tells me which context this file is running in.")
print("The value of __name__ is:", repr(__name__))

print("This is my file to demonstrate best practices.")

# a melhoor forma de criar um script seria essa
# criar codigo em algum lugar, criar um metodo main pra rodar esse codigo criado
# e dps chamar o metodo main diretamente no arquivo main.py por ex.
# descrito dessa forma abaixo.


def process_data(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data


def main():
    data = "My data read from the Web"
    print(data)
    modified_data = process_data(data)
    print(modified_data)


if __name__ == "__main__":
    main()
