# https://docs.pydantic.dev/usage/models/#field-ordering
# Conforme demonstrado pelo exemplo acima, combinar o uso de campos anotados e
#  não anotados no mesmo modelo pode resultar em ordenações surpreendentes de campos.
#  (Isto é devido a limitações do Python)
# Portanto, recomendamos adicionar anotações de tipo a todos os campos,
#  mesmo quando um valor padrão determinar o tipo por si só para garantir
#  que a ordem dos campos seja preservada.
#
# Isso acontece cmg bastante, dos fields se "perderem", e eles explicam aqui o porque
# e como fazer para contornar isso.
# # ---------------------------------------


# parei aqui nas dicas do pydentic
#  https://docs.pydantic.dev/usage/models/#required-optional-fields
