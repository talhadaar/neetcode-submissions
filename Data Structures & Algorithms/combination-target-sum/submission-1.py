class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Make combinatios of nums from nums where they sum to target
        # Can pick a number however many times
        # Combinations must be unique(order doesn't matter for equality)

        # Backtracking
        # At each nums[i] keep chosing it, or move to next
        # basecase: sum>target return and exclude this number, pick next, if sum==target, add combination to result

        # [2,5,6,9]
        # 2,4,6,8,10
        res = []
        combination = []
        n = len(nums)

        def dfs(i, totalSum):
            if totalSum==target:
                res.append(combination.copy())
                return
            if totalSum>target or i>=n:
                return

            # pick this number into solution
            combination.append(nums[i])
            # pick again if possible
            dfs(i, totalSum+nums[i])

            # remove this number, make alternative choice
            combination.pop()
            # if not, pick next number
            dfs(i+1, totalSum)

        dfs(0,0)
        return res