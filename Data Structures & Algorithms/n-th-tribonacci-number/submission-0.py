class Solution:
    def tribonacci(self, n: int) -> int:
        dp = deque([0,1,1])
        if n < 3:
            return dp[n]

        for i in range(2,n):
            tn = sum(dp)
            dp.popleft()
            dp.append(tn)

        return dp.pop()
