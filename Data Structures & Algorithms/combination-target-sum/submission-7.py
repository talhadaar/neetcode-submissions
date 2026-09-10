class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # Backtracking
        # Make all combinations and check their sums
        # if sum==target: add to result

        res = []
        combination = []
        n = len(nums)

        def dfs(i, sum):
            # target hit, nice
            # undo choice and move on to next
            if sum==target:
                res.append(combination.copy())
                return

            # No more choices to be made or bad choices
            if i>=n or sum>target:
                return
    
            # chose current item and move on with it
            # can chose i however many times
            combination.append(nums[i])
            dfs(i, sum+nums[i])

            # undo choice, go to next
            combination.pop()
            dfs(i+1, sum)

        dfs(0, 0)
        
        return res