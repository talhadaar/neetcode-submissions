class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking - Pick a number or skip it, when returning, try another number
        # we will get all possibilities between no choice at all at any slot, and different choices at every slot so to speak, between [] and [1,2,3]
        res = []
        subset = []
        n = len(nums)

        def dfs(i):
            # no more slots
            if i>=n:
                print(subset)
                res.append(subset.copy())
                return

            # at ths slot, pick this number
            subset.append(nums[i])
            dfs(i+1)
            # reset slot, try next number
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res