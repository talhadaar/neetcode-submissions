class Solution:
    def rob(self, nums: List[int]) -> int:
        # at i'th house: cannot have robbed(i, i+1) or rob(i, i-1)
        # Assumption: cannot modify nums[]

        # Maximize the score by: Robbing the current or skipping it
        # Decision: Rob or skip to maximize

        # DFS: Explores all possible solutions
        # Base case to rewind recursive stack
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     return max(dfs(i+1), nums[i]+dfs(i+2))

        # DFS with Memoization: Use memoization to reduce subproblems
        # memo = [-1] * len(nums) # Max score at a house
        # def dfs(i):
        #     # Base case to rewind recursive stack
        #     if i >= len(nums):
        #         return 0
        
        #     if memo[i]!=-1:
        #         return memo[i]

        #     # update memo with new max score
        #     memo[i] = max(dfs(i+1), nums[i]+dfs(i+2))
        #     return memo[i]

        # DP bottom up: Keep track of max score upto i-1 and i-2
        # At i, either: not rob -> score is still i-1th score
        # or rob: score is i + i-2th score
        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]

        # dp = [0] * len(nums)
        # # No choice to make at 1st house
        # dp[0] = nums[0]
        # # at 2nd house, maximize score
        # dp[1] = max(nums[0], nums[1])

        # # maximize score at 3rd house and onwards
        # for i in range(2, len(nums)):
        #     # nums[i]+dp[0]: Rob house and i-2th
        #     # dp[1]: Skip i'th and rob adjacent
        #     dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        # return dp[-1]

        # DP: space optimized
        # Only need to know the i-1 and i-2th score
        robA, robB = 0,0
        for num in nums:
            maxRob = max(robA+num, robB)
            # shift scores
            robA = robB
            robB=maxRob
        # robB is the maxScore upto latest house
        return robB