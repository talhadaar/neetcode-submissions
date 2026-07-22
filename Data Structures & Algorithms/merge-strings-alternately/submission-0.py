class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n,m = len(word1), len(word2)
        res = ""

        for i in range(max(n,m)):
            if i < n:
                res += word1[i]
            if i < m:
                res += word2[i]
        
        return res