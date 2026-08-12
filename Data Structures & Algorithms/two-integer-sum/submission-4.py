class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for idx,num in enumerate(nums):
            hmap[num] = idx

        for idx,num in enumerate(nums):
            diff = target - num
            if diff in hmap and hmap[diff] != idx:
                return [idx, hmap[diff]]
        return []