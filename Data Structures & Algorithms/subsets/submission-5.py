class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking
        # At each i, we can chose to include it or no
        # each choice will make 1 subset
        # we make a choice n times

        res = []
        subset = []
        n = len(nums)

        def dfs(i):
            if i >= n:
                res.append(subset.copy())
                return
            # choice: pick this one and move on
            subset.append(nums[i])
            dfs(i+1)

            # choice: don't pick and move on
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res