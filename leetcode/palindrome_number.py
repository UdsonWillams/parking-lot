class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            str_x = str(x)
            reversed_str_x = str_x[::-1]
            if str_x == reversed_str_x:
                return True
        return False
