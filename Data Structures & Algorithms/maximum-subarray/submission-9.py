class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Recursion: Make all subarrays and check
        # We can pick nums i and increment total or skip it

        maxSub,currSum = nums[0],0

        for num in nums:
            if currSum<0:
                currSum = 0
            currSum +=num
            maxSub = max(maxSub, currSum)
        return maxSub