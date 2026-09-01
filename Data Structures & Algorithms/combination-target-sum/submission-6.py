class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
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