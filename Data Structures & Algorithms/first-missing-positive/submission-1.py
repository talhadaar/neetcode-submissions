class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        # do a cycle sort
        while i < n:
            # ignore negative nums or out of bounds nums
            # these cant be answers
            if nums[i] <= 0 or nums[i] > n:
                i+=1
                continue

            # 1 will at i=0, 4 will be at i=3
            index = nums[i] - 1

            # if not duplicate then cycle
            if nums[i] != nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
            # if duplicate then ignore
            else:
                i+=1

        # first i where num is not i + 1 is the missing number
        for i in range(n):
            if nums[i] != i+1:
                return i+1

        return n + 1