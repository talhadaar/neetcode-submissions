class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Make combinatios of nums from nums where they sum to target
        # Can pick a number however many times
        # Combinations must be unique(order doesn't matter for equality)

        # Backtracking
        # At each nums[i] keep chosing it, or move to next
        # basecase: sum>target return and exclude this number, pick next, if sum==target, add combination to result

        # Optimize: Sort the nums

        # [2,5,6,9]
        # 2,4,6,8,10
        res = []
        combination = []
        n = len(nums)
        nums.sort()

        def dfs(i, totalSum):
            if totalSum==target:
                res.append(combination.copy())
                return

            for j in range(i, n):
                if totalSum+nums[j] > target:
                    return

                combination.append(nums[j])
                dfs(j, totalSum+nums[j])
                combination.pop()

        dfs(0,0)
        return res