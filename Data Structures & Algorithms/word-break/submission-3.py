class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        # If we found a word starting at i, can the rest(suffix) be segmented?
        # subproblem: can suffix s[i:] be segmented? revisited many times

        n = len(s)
        memo = defaultdict(bool)
        memo[n] = True

        def dfs(i):
            if i == n:
                return True
            if i in memo:
                return memo[i]

            for word in wordDict:
                m = len(word)
                if i+m<=n and s[i:i+m] == word:
                    if dfs(i+m):
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        return dfs(0)