class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestIdx = 0
        longestLen = 0
        LEN = len(s)
        for i in range(LEN):
            # odd length
            l,r = i,i
            # expand
            while l>=0 and r<LEN and s[l]==s[r]:
                substrLen = r-l+1
                if substrLen > longestLen:
                    longestIdx = l
                    longestLen = substrLen
                l-=1
                r+=1

            # even length
            l,r = i,i+1
            while l>=0 and r<LEN and s[l]==s[r]:
                    substrLen = r-l+1
                    if substrLen > longestLen:
                        longestIdx = l
                        longestLen = substrLen
                    l-=1
                    r+=1
                
        return s[longestIdx: longestIdx + longestLen]
