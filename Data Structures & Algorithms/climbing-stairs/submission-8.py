class Solution:
    def climbStairs(self, n: int) -> int:
        # We only need track ways to reach i+1 and i+2 stair
        # current one is the sum of both

        dp = [0,1]

        for i in range(1,n+1):
            t = dp[1]
            dp[1] = dp[0]+dp[1]
            dp[0] = t
        return dp[1]