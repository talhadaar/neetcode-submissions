class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Substring: Contiguous memory.

        # Find all substrings without dupes
        # O(N*N) for substrings

        # 2 Pointers:
        # l=r=0, Extend right until a repeating char is seen
        # remove l from set, and attempt to add r to set
        # if l ==r, we look for a new substring now

        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res