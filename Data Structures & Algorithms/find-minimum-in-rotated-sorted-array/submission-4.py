class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Min element is the pivot
        # find the pivot, find the element
        # if r>mid>l, then we find the pivot
        # [3,4,5,6,1,2]

        n = len(nums)
        l,r=0,n-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]<nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]