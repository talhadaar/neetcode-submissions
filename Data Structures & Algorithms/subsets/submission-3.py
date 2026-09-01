class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking
        # Build all possible subsets
        # At every i:
        # Include current number and move on or exclude and move on
        # for an empty subset, we can at min, chose no nums after seeing all or chose all after seeing all
        # and make different combinations of them
        # when i>=n, we have made all possible choices and arrived at a possible result

        res = []
        subset = []
        n = len(nums)

        def dfs(i):
            # No more choices to make at current point in problem space
            # so we have a possible result
            if i>=n:
                res.append(subset.copy())
                return

            # at this i, we can: Pick and move forward
            subset.append(nums[i])
            dfs(i+1)
            # exclude this i and move forward
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res