class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force: Extend a pointer from eacn prices[i]
        # O(N*N)

        # 2 Pointers
        # l look for lowest price, r look for higher
        res, low = 0, float('inf')
        for p in prices:
            low = min(low, p)
            res = max(res, p - low)
        return res 