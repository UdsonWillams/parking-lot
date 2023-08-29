from re import match


def match_patterns_with_regex(path):
    """
    Verifica se o valor passado bate com o padrão já estabelecido.
    """
    pattern = r"^/api/v1/users/[0-9]+/$"
    if match(pattern, path):
        return True
    return False


print(match_patterns_with_regex("/api/v1/users/123321/"))
print(match_patterns_with_regex("/api/v1/users/aaa/"))
print(match_patterns_with_regex("/api/v1/users/==-=-/"))
print("OUTROS VALORES >>>")

# outra forma de fazer seria com o \d no lugar do [0-9]
