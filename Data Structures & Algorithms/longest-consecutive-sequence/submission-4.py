class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Longest consequtive sequence - longest sequnce we can make from numbers in nums
        # can be anywhere in nums
        # Brute Force: sorting and checking

        # For every number, check if a previous or next number was seen before and at what index
        # then each number will be a tuple (num, prevNumIndex)- stitch these tuples into one list of longest consecutive sequence

        numSet = set(nums)
        res = 0
        n = len(nums)
        for num in nums:
            if (num-1) not in numSet:
                l = 1
                while (num+l) in numSet:
                    l+=1
                res = max(res, l)
        return res
