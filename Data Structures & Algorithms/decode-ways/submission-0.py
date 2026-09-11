class Solution:
    def numDecodings(self, s: str) -> int:
        # Number of ways to decode a string
        # Numbers to letters
        # We have a choice: we can pick singleton or a pair
        # A - pick(s[i]) - just this one
        # B - pick(s[i:i+2]) - this and next to make a pair
        # if s[i] is 0 or s[i:i+2]<10, invlaid
        # I ask: if i pick s[i] can i decode the whole thing?
        # If i pick[i:i+2] can i decode the whole thing?

        n = len(s)
        # At any i, i would have calculated number of ways already, so i can cache them
        cache = defaultdict(int)
        cache[n] = 1
        def dfs(i):
            if i in cache:
                return cache[i]

            if s[i] == '0':
                return 0

            # pick all singletons
            res = dfs(i+1)
            # lets try picking pairs of whatever was left
            if i < n-1:
                if (s[i]=='1' or (s[i]=='2' and s[i+1]<'7')):
                    res+=dfs(i+2)
            cache[i] = res
            return res

        return dfs(0)