import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 + str2 != str2 + str1):
            return ''
        return str1[:math.gcd(len(str1), len(str2))]

        """
        g = math.gcd(len(str1), len(str2))
        x = str1[:g]
        if str1 == x * (len(str1)//len(x)) and str2 == x * (len(str2)//len(x)):
            return x
        else:
            return ""
        """
        
