class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        tfmap = defaultdict(int)
        for c in t:
            tfmap[c]+=1

        window = defaultdict(int)
        have,need = 0, len(tfmap)
        res,resLen =[-1,-1], float('inf')
        l = 0
        # roll r on and count freq of chars seen in window
        for r in range(len(s)):
            c = s[r]
            window[c]+=1

            # if freq of char seen == freq required by t
            # we have found 1 item
            if c in tfmap and window[c] == tfmap[c]:
                have+=1

            # incase we've found the while thing in this window
            # let's try squeezing it by moving l up
            while have==need:
                newLen = r-l+1
                if newLen < resLen:
                    res = [l,r]
                    resLen = newLen

                # discount the removed s[l] frequency
                window[s[l]]-=1
                # if this was a item required by t, adjust
                if s[l] in tfmap and window[s[l]]<tfmap[s[l]]:
                    have-=1
                # finally move up l
                l+=1
        l,r = res
        return s[l : r + 1] if resLen != float("infinity") else ""