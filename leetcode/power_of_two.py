class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
        return True
# Fica verificando se o valor é sempre  dividivel por 2. 
# Se em apenas um valor o retorno não for %2 == 0 já retorna false.
