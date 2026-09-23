class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Alternative: Use hashmaps to count how many times a number is left to chose from

        fmap = Counter(candidates)
        nums = [num for num in fmap.keys()] # unique numbers

        res = []
        path = []
        n = len(nums)

        def dfs(i, need):
            # cannot pick this number again for this combo
            if need == 0:
                res.append(path.copy())
                return
            
            if need<0 or i >= n:
                return
                
            num = nums[i]
            if fmap[num] > 0:
                fmap[num] -= 1
                path.append(num)
                dfs(i, need - num)
                path.pop()
                fmap[num] += 1
            dfs(i + 1, need)

        dfs(0,target)
        return res