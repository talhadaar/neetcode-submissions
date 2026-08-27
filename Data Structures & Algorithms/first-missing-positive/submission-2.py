class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Concern with positive ints only, discard negatives and zeros
        # nums of len n, there must be n positive ints in the array or [1..n]
        # Cycle Sort: Replace negatives with 0, and place positives in appropirate positions
        # if first 0 is seen at i'th position, then missing num is i+1

        # [1,2,4]
        # [1,2,0]


        n = len(nums)

        def cycleSort(nums):
            i=0
            while i < n:
                # Continue if out of bounds or invalid num
                if nums[i]<=0 or nums[i]>n:
                    i+=1
                    continue

                
                # deal with cycling nums
                idx = nums[i] - 1
                if nums[idx] != nums[i]:
                    nums[idx],nums[i] = nums[i], nums[idx]
                else: # if correct already we move on
                    i+=1

        cycleSort(nums)
        for i in range(n):
            if nums[i] != i+1:
                return i+1

        return n+1