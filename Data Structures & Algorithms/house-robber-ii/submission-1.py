class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        flag = [False]

        if n == 1:
            return nums[0]

        memo = [[False]* 2 for _ in range(n)]

        def dfs(i, flag):
            if i>=n or (flag and i==n-1):
                return 0

            if memo[i][flag]:
                return memo[i][flag]
            
            memo[i][flag] = max(nums[i] + dfs(i+2, flag or i==0), dfs(i+1, flag))
            return memo[i][flag]
            
        return max(dfs(0, True), dfs(1, False))