class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while a>0 or b>0 or c>0:
            a_i = a & 1
            b_i = b & 1
            c_i = c & 1

            if ((c_i == 1) & (a_i | b_i == 0)):
                res = res + 1
            elif ((c_i == 0) & (a_i | b_i == 1)):
                res += a_i + b_i

            a >>= 1
            b >>= 1
            c >>= 1

        return res