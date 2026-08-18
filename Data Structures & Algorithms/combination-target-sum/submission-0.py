class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        # DFS/Backtracking
        # Add i'th num to path(again) if path sum is valid or leave it and add i+1th
        # if i+1th num makes sum invlaide, no need to search further in a path.

        nums.sort()
        res = []

        def dfs(idx, path, tsum):
            # Success basecase
            if tsum == target:
                res.append(path.copy())
                return

            for i in range(idx, len(nums)):
                if tsum+nums[i] > target:
                    return
                # Continue testing with current number
                path.append(nums[i])
                dfs(i, path, tsum+nums[i]) # returns after having tested with 1 number only
                path.pop()

        dfs(0,[],0)
        return res