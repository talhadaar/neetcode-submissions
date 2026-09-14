class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Of ways to reach grid[m][n] = grid[m-1][n] + grid[m][n-1]
        dp = [1] * n
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[j] += dp[j + 1]

        return dp[0]