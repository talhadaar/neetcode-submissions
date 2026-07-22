class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxP = 0

        for price in prices:
            p = price - minBuy
            if p > maxP:
                maxP = p
            if price < minBuy:
                minBuy = price

        return maxP