class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, perm, used=[],[],set()
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for idx,num in enumerate(nums):
                if idx in used:
                    continue

                perm.append(num)
                used.add(idx)
                dfs()
                perm.pop()
                used.remove(idx)
        dfs()
        return res