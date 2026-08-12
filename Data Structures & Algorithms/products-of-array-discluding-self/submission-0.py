class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        LEN = len(nums)
        prefix = [0] * LEN
        suffix = [0] * LEN
        # results array
        res = [0] * LEN

        # nothing to left of nums[0]
        prefix[0] = 1
        # build prefix prods
        for i in range(1, LEN):
            prefix[i] = prefix[i-1] * nums[i-1]

        # nothing to right of nums[LEN+1]
        suffix[LEN - 1] = 1
        # build suffix prods
        for i in range(LEN - 2,-1,-1):
            suffix[i] = nums[i+1] * suffix[i+1]

        for i in range(LEN):
            res[i] = suffix[i] * prefix[i]
        return res