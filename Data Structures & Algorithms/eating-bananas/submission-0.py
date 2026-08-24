class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r

        while l<=r:
            k = (l+r)//2

            totalTime = 0
            # calculate total time taken to eat all piles at this speed
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            # if this k is valid(fast enough), go to find smaller k
            if totalTime <= h:
                res = k
                r = k - 1
            # if k was invalid(too slow), search a larger k
            else:
                l = k + 1
        return res