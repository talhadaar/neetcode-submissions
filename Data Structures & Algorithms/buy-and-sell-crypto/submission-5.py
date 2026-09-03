class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force: Extend a pointer from eacn prices[i]
        # O(N*N)

        # 2 Pointers
        # l look for lowest price, r look for higher
        l,r=0,1
        res = 0

        while r<len(prices):
            if prices[l]<prices[r]:
                p = prices[r]-prices[l]
                res = max(res, p)
            else:
                l = r
            r+=1
        return res