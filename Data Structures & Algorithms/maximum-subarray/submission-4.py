class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kdane's algo: If currSum of subarray is negative, reset total and move on

        currSum = 0
        maxSum = nums[0]

        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum+=num
            maxSum = max(currSum, maxSum)
        return maxSum