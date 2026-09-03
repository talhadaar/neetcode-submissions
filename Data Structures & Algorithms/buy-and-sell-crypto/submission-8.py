class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, low = 0, float('inf')
        for p in prices:
            low = min(low, p)
            res = max(res, p - low)
        return res