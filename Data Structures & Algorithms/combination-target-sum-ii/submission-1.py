class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Can have duplicates in candidates: Which means 1 number can be picked twice for a solution, but it must be picked at most 1

        res = []
        solution = []
        n = len(candidates)
        candidates.sort()

        def dfs(i, totalSum):
            if totalSum==target:
                res.append(solution.copy())
                return

            # sum exceedes target or no more choices to make
            if totalSum>target or i==n:
                return

            # pick this number and move to next
            solution.append(candidates[i])
            dfs(i+1, totalSum+candidates[i])

            # skip this number and it's duplicates
            solution.pop()
            while i+1<n and candidates[i] == candidates[i+1]:
                i+=1
            # skip this number, don't carry it forward into the sum
            dfs(i+1, totalSum)
            
        dfs(0,0)
        return res