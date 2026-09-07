class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h hours to eat all the bananas
        # find k(bananas per hour) to eat all bananas within h hours
        # Can only eat 1 pile in an hour

        # Can we finish at k speeds? 
        # Test at different speeds
        # min: 1 banana per hour, max: max(piles) bananas per hour

        l,r = 1,max(piles)
        while l<=r:
            k = (l+r)//2

            # total hours needed to finish at this speed
            totaltime = 0
            for p in piles:
                totaltime+=math.ceil(float(p)/k)
            if totaltime<=h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res
