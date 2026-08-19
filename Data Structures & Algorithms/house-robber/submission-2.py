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

        # Use memoization to reduce subproblems
        memo = [-1] * len(nums) # Max score at a house

        def dfs(i):
            # Base case to rewind recursive stack
            if i >= len(nums):
                return 0
        
            if memo[i]!=-1:
                return memo[i]

            # update memo with new max score
            memo[i] = max(dfs(i+1), nums[i]+dfs(i+2))
            return memo[i]

        return dfs(0)