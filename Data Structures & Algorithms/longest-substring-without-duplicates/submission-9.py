class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in lastSeen:
                # It's possible to have seen this char outside of current window
                # so record is stale
                # so we keep standing at l
                l = max(lastSeen[s[r]] + 1, l)
            lastSeen[s[r]] = r
            res = max(res, r-l+1)
        return res