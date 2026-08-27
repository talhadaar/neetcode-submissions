class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force: Check every i'th against every other i'th number

        # Sorted array: 2 ptr

        # nums[i] + nums[j] = target
        # nums[j] = target - nums[i] - complement of nums[j]
        # Track every num seen so far and its idx in a map
        # If complement of a num is in the map, it is the i'th idx required

        compelements = defaultdict(int)
        for idx,num in enumerate(nums):
            comp = target - num
            if comp in compelements:
                return [compelements[comp], idx]
            compelements[num] = idx