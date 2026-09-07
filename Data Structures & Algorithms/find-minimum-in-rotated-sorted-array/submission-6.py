class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Min value is the pivot i where nums[i-1]>nums[i]<nums[i+1]
        # We need to find the pivot
        # [1,2,3,4,5,6]
        # [3,4,5,6,1,2]

        # O(N): Iter and nums[i] that satisfies nums[i-1]>nums[i]<nums[i+1]
        l,r=0,len(nums)-1
        while l<r:
            mid = (l+r) // 2
            if nums[mid]<nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]