class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Find banas per hour,k, to eat all bananas within h

        # Test for k over piles
        # Binary search over k [1..MAX_PILE]
        low,high = 1, max(piles) # O(?) of max([])?

        k = 0
        while low<=high:
            k = low + (high-low) //2

            timeTaken = 0
            for pile in piles:
                timeTaken+=math.ceil(float(pile)/k)
            if timeTaken<=h:
                res = k
                high = k - 1
            elif timeTaken>h:
                low = k + 1

        return res