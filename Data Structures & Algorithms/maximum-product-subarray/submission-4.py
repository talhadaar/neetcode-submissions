class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kdane's
        # A nums[i]==0 ends a run
        # track maxProd and minProd
        # because a negative num can maximize minProd

        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            res = max(res, curMax)
        return res