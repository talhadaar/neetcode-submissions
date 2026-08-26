class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,res = 0,0
        charmap = {}
        for r in range(len(s)):
            # if any char reoccurs, we squeeze window
            # move window to AFTER l'th dupe
            if s[r] in charmap:
                l = max(charmap[s[r]]+1, l)
            charmap[s[r]] = r
            res = max(res, r-l+1)
        return res