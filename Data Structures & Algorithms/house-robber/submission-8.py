class Solution:
    def rob(self, nums: List[int]) -> int:
        # Cannot rob 2 adjacent houses
        # Choice: Rob or skip current house, based on if previous house was robbed

        n = len(nums)
        memo = defaultdict(int)
        def dfs(i):
            if i>=n:
                return 0
            if i in memo:
                return memo[i]
            memo[i] =  max(dfs(i+1), nums[i]+dfs(i+2))
            return memo[i]

        return dfs(0)