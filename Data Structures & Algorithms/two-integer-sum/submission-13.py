class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        idxMap = {}
        for idx, num in enumerate(nums):
            diff = target-num
            if diff in idxMap:
                return [idxMap[diff], idx]
            idxMap[num] = idx
