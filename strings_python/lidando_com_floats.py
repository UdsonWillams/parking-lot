print(f"One third, rounded to two decimal places is: {1 / 3:.2f}")

# Podemos separar os valores do float com a expressão :
# Com ele separamos os campos e retornamos o valor arredondado para 2 casas deciamis.

print(f"One third, rounded to two decimal places is: {1000:,.2f}")
# outro exemplo, adicionando uma virgula e deixando o valor com um melhor retorno.
# Aqui dizemos que o 1000 vai ter uma , e depois do ponto flutuante mais 2 casas.
# Logo o retorno fica 1,000.00

## Alguns exemplos utilizando valores
print(f"{0.1256:.1%}")
print(f"{0.5:.2%}")
print(f"{3:.2%}")

# COmo centralizar os valores, ou mover pra um lado especifico.
sample = 12345.6789
print(
f"(1) |{sample:<12,.2f}|", # left
f"(2) |{sample:>12,.2f}|", # right
f"(3) |{sample:^12,.2f}|", # center
sep="\n",)


# mais exemplos :
# https://realpython.com/how-to-python-f-string-format-float/#how-to-format-and-round-a-float-within-a-python-f-string
