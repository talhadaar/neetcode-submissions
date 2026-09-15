class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, combination, totalSum):
            if totalSum == target:
                res.append(combination.copy())
                return

            for j in range(i, len(candidates)):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                if totalSum + candidates[j] > target:
                    break
    
                # pick this number and move on
                combination.append(candidates[j])
                dfs(j+1, combination, totalSum+candidates[j])
                combination.pop()

        dfs(0,[],0)
        return res