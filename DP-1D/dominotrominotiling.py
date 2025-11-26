class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7
        if n == 0: return 1
        if n == 1: return 1
        if n == 2: return 2

        f0, f1, f2 = 1, 1, 2

        for i in range(3, n+1):
            fn = (2 * f2 + f0) % mod
            f0, f1, f2 = f1, f2, fn

        return f2