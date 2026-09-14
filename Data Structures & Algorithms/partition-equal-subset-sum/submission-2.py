class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Make 2 subsets where both have the same sum
        # All elements must be used, but not reused.
        # No Duplicates?

        # Target is a state: A sum where 2 subsets can fit

        # Recursively: Make subsets, if all sum//2==0, it's possible

        total = sum(nums)
        if total%2:
            return False

        n = len(nums)
        cache = defaultdict(int)

        def dfs(i, s):
            if i >=n:
                return s == 0
            if s<0:
                return False
            if (i,s) in cache:
                return cache[(i,s)]
            # Skip number or include it to reduce target
            cache[(i,s)] = dfs(i+1, s) or dfs(i+1, s-nums[i])
            return cache[(i,s)]
        return dfs(0, total//2)