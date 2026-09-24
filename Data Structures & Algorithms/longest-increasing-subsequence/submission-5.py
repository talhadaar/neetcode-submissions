class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP top down:
        # Increase a number or skip if if it's not larger than the last
        cache = {}
        def dfs(current,last):
            if current == len(nums):
                return 0

            if (current,last) in cache:
                return cache[(current,last)]
            # skip all the way to end
            cache[(current,last)] = dfs(current+1, last)
            
            if last == -1 or nums[last]<nums[current]:
                cache[(current,last)] = max(cache[(current,last)], 1+ dfs(current+1, current))

            return cache[(current,last)]

        return dfs(0,-1)