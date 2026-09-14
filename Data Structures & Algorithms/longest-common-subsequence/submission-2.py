class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        t1Len = len(text1)
        t2Len = len(text2)

        cache = {}
        def dfs(i,j):
            if i == t1Len or j==t2Len:
                return 0

            if (i,j) in cache:
                return cache[(i,j)]
            if text1[i] == text2[j]:
                cache[(i,j)] =  1 + dfs(i+1,j+1)
            else:
                cache[(i,j)] = max(dfs(i+1, j), dfs(i, j+1))
            
            return cache[(i,j)]

        return dfs(0,0)