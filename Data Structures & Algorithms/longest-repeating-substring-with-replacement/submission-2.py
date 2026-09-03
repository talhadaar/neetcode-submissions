class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # In any window W, with most repeating char C, we need to replace at most k
        # so, if len(W)-freq(C) <=k, we can do replacements in this window.
        # So we find the largest window that satisfies len(W)-freq(C) <=k

        count = defaultdict(int)
        res = 0

        l=window=0

        for r in range(len(s)):
            # count char occurance
            count[s[r]]+=1
            # most recurring char frequency
            window = max(window, count[s[r]])


            # if window exceedes required size, squeeze until we have a valid window
            while (r-l+1) - window > k:
                count[s[l]]-=1
                l+=1

            res = max(res, r-l+1)
        return res