class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastSeen = {s[0]:0}
        for i,c in enumerate(s):
            lastSeen[c] = i

        l,r =0,0
        n = len(s)
        res = []
        max_idx = 0
        while r < n:
            max_idx = max(max_idx, lastSeen[s[r]])
            if r == max_idx:
                res.append(r-l+1)
                l = r+1
            r += 1
        return res