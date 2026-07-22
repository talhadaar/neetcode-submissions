class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0

        i = 1
        n = len(prices)

        while i < n:
            if prices[i] > prices[i - 1]:
                p += (prices[i] - prices[i-1])
            i+=1
        return p