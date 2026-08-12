class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Calculate prefixes in a results array
        LEN = len(nums)
        res = [1] * LEN

        # prefix of nums[0] is nothing
        prefix = 1
        for i in range(0, LEN):
            # place prefix of current num in its place
            res[i] = prefix
            # calc next for next num
            prefix*=nums[i]

        # suffix of nums[LEN-1] is nothing
        suffix = 1
        for i in range(LEN-1, -1,-1):
            # res[i] = prefix of that num * suffix of that num
            res[i]*=suffix
            # calculate suffix of this num
            suffix*=nums[i]

        return res