def isValid(s: str) -> bool:
    """
    :type s: str - String to be tested for validity
    :rtype: bool - Returns true if the string is valid else false
    """
    dct = {")": "(", "]":"[", "}": "{"}
    pilha = []
    for i in s:
        if i in dct:
            topo = pilha.pop() if pilha else "%"            
            if dct[i] != topo:
                return False
        else:
            pilha.append(i)

    return not pilha


if __name__ == "__main__":
    line = input()
    if isValid(line):
        print("valid")
    else:
        print("invalid")
