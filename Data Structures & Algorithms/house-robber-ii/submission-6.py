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

            # score at i-2
            rob1 = 0
            # score at i-1
            rob2 = 0

            for num in nums:
                # which of 2 decisions gives max score
                tmp = max(rob2, num+rob1)
                rob1 = rob2
                rob2 = tmp

            return rob2
        
        if len(nums) == 1:
            return nums[0]
        return max(dp(nums[1:]), dp(nums[:-1]))