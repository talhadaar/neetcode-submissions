class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # Entirity of s must be segmented
        # different subarrays of s can exist in worddict
        # so we can have different ways to segment
        # we must only return if it's possible

        
        words = set(wordDict)
        n = len(s)
        t = 0
        for w in wordDict:
            t = max(t, len(w))
    
        memo = defaultdict(bool)

        def dfs(i):
            if i in memo:
                return memo[i]
            if i==n:
                return True

            for j in range(i, min(n, i+t)):
                if s[i:j+1] in words:
                    if dfs(j+1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dfs(0)