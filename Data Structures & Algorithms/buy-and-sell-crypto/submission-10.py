class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, low = 0, float('inf')
        for p in prices:
            # track the min seen so far
            low = min(low, p)
            # res is current price - lowest seen so far
            res = max(res, p - low)
        return res