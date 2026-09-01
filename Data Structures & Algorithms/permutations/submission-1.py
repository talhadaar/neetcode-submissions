class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res, path, used = [],[],set()

        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i,n in enumerate(nums):
                # i'th number already used for path
                if i in used:
                    continue

                used.add(i)
                path.append(n)
                dfs()
                path.pop()
                used.remove(i)
        dfs()
        return res