class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kdane's Algo

        maxSum, currSum = nums[0], 0

        for num in nums:
            currSum = max(num, currSum + num)
            maxSum = max(maxSum, currSum)

        return maxSum