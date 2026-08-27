class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force: ignore i'th and prod all else O(n*n)
        # use 2ptrs to optimise this

        # Take product of all array
        # Divide away i'th num to get product except self
        # [1,4,5,0,4,2] <- 1 zero means result will have 1 product
        # [12,3,4,5,0,2,3,0] <- more than 1 zero means everything is zero
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt +=  1
        if zero_cnt > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt: res[i] = 0 if c else prod
            else: res[i] = prod // c
        return res