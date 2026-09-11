class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kdane's
        # A nums[i]==0 ends a run
        # track maxProd and minProd
        # because nums[i]<0 can make minProd the max

        res = nums[0]
        currMax,currMin = 1,1

        for num in nums:
            tmp = currMax * num
            currMax = max(num*currMax, num*currMin, num)
            currMin = min(tmp, num*currMin, num)
            res = max(res, currMax)
        return res
