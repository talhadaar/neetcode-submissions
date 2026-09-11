class Solution:
    def climbStairs(self, n: int) -> int:
        # Backtracking: Can take 2 or 1 step to current stair
        memo = defaultdict(int)

        def climb(i):
            if i>=n:
                return i==n

            if i in memo:
                return memo[i]
            memo[i] = climb(i+1) + climb(i+2)
            return memo[i]
        return climb(0)