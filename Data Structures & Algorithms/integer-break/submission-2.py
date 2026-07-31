class Solution:
    def integerBreak(self, n: int) -> int:
        if n <=3:
            return n-1

        res = 1
        # ...+3+1 not optimal, 2+2 yes optimal
        while n > 4:
            res*=3
            n-=3
        return res * n