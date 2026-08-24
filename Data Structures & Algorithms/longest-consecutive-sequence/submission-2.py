class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [2,20,4,10,3,4,5]
        # num can be start of sequence if n-1 doesn't exist
        numsSet = set(nums)
        longest = 0

        for num in numsSet:
            # if num-1 not in set, then its start of a sequence possibly
            if (num - 1) not in numsSet:
                length = 1
                while (num + length) in numsSet:
                    length +=1
                longest = max(length, longest)
        return longest