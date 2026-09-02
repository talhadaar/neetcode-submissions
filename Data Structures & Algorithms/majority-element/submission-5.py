class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = candidate = 0
        for num in nums:
            if count == 0:
                candidate = num
            count+=1 if candidate==num else -1
        # Considering the case that a majority doesn't exist
        return candidate if nums.count(candidate) *2 > len(nums) else None