class Solution:
    def numDecodings(self, s: str) -> int:

        # 0 and 0x is an invalid pick
        # greedily pick all singletons then pick pairs of what was left
        
        n = len(s)
        cache = defaultdict(int)
        cache[n] = 1
        def dfs(i):
            if i in cache:
                return cache[i]

            if s[i] == '0':
                return 0

            res = dfs(i+1)

            if i < n-1:
                if (s[i]=='1' or (s[i]=='2' and s[i+1]<'7')):
                    res+=dfs(i+2)
            cache[i] = res
            return res

        return dfs(0)