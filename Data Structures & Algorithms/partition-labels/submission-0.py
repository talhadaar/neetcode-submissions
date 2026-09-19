class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # partition into substrings, such that, any letter in s, appears in at  most 1 substring and no other

        # abcabc
        # cannot do abc abc, each character appears more than once
        # not possible to split

        # Partition into substring, check each char in substring appear no where else
        # len of any substring: max(last occurance of any element in this substring)

        # 0x 1y 2x 3x 4y 5z 6b 7z 8b 9b 10i 11s 12l
        # x = 3, y = 4, z=7, b=9, i=10,s=11,l=12
        # O(N)
        
        # calculate last occurances
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