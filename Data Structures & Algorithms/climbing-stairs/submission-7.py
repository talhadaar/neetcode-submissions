class Solution:
    def climbStairs(self, n: int) -> int:
        # Recursive DFS: Too inefficient O(2^n) time and O(n)
        # Memoization dynamic top down(recursive): O(n) and O(n)
        # Bottom Up DP: 

        # 5
        # 1-> 1
        # 2-> 2
        # 3 -> 3
        # 4 -> 3+2 5
        # 5 -> 5+3 8

        if n <=2:
            return n

        dp = [1,2]
        for i in range(3, n+1):
            t = sum(dp)
            dp[0] = dp[1]
            dp[1] = t

        return dp[1]