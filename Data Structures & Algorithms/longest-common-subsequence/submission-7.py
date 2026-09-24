class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Top Down DP
        n = len(text2)
        dp = [0] * (n+1)

        for w1 in range(len(text1)):
            prev = 0
            for w2 in range(len(text2)):
                temp = dp[w2+1]
                if text1[w1] == text2[w2]:
                    dp[w2+1] = 1 + prev
                else:
                    dp[w2+1] = max(dp[w2+1], dp[w2])
                prev = temp
        return dp[n]