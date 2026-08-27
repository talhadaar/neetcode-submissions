class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute Force:
        # All possible subarrays, find the longest that is a consecutive sequence
        # DFS: look ahead for nums[i]+1, check all possible values at every possible nums[i]

        # Sort and search O(n+nLogn)

        # HashSet
        # if num-1 not in set: Implies it's the start of sequence
        # Iterate to find the next nums for as far as possible

        hset = set(nums)
        longest = 0

        for num in hset:
            if (num-1) not in hset:
                l = 0
                while (num+l) in hset:
                    l+=1
                longest = max(l, longest)
        return longest