class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Substring: Contiguous memory.

        # Find all substrings without dupes
        # O(N*N) for substrings

        # 2 Pointers:
        # l=r=0, Extend right until a repeating char is seen
        # remove l from set, and attempt to add r to set
        # if l ==r, we look for a new substring now

        lastSeen = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in lastSeen:
                # locate the prev dupe and start from after it
                l = max(lastSeen[s[r]] + 1, l)
            lastSeen[s[r]] = r
            res = max(res, r-l+1)
        return res