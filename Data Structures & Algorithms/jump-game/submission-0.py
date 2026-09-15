class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]

            # Reached the finish line
            if i==n-1:
                return True

            # Cannot jump 0 distance if not EOL
            if nums[i] == 0:
                return False

            # farthest idx can jump to
            last = min(n, i + nums[i]+1)

            # from next till last
            for j in range(i+1,last):
                if dfs(j):
                    cache[i] = True
                    return True
            cache[i] = False
            return False

        return dfs(0)