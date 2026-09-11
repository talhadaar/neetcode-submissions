class Solution:
    def rob(self, nums: List[int]) -> int:
        # [2,9,8,3,6]
        # Array is circular: so cannot rob nums[0] and nums[-1] in the same decision tree
        # Only constraint to work against.
        # Subproblems: in both decision trees, subproblems can reoccur
        n = len(nums)
        if n == 1:
            return nums[0]
            
        memo = [[False] * n for _ in range(n)]

        def dfs(i, flag):
            if i>=n or (flag and i==n-1):
                return 0

            if memo[i][flag]:
                return memo[i][flag]

            memo[i][flag] = max(dfs(i+1, flag), nums[i]+dfs(i+2, flag or i==0))
            return memo[i][flag]
        return max(dfs(0, True), dfs(1, False))