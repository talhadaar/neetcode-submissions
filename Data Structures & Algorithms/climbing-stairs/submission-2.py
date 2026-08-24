class Solution:
    def climbStairs(self, n: int) -> int:
        # Number of ways to reach i is always the same, just in different order
        # so we cache the ways
        cache = [-1] * n
        def dfs(i):
            # return wether solution is valid/invalid
            if i >= n:
                return i == n
            # if path was cached already, just return it
            if cache[i] != -1:
                return cache[i]
            # add new path to cache
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0)