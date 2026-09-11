class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP Top Down
        # rob i+1 or i+2
        # for [1:-1] and [0:-2]

        def dp(nums: List[nums]) -> int:
            if not nums:
                return 0

            n = len(nums)
            if n == 1:
                return nums[0]

            dp = [0]*n
            # max score so far at house 0
            dp[0] = nums[0]
            # max score so far at house 1
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i-1], nums[i]+dp[i-2])

            return dp[-1]
        
        if len(nums) == 1:
            return nums[0]
        return max(dp(nums[1:]), dp(nums[:-1]))