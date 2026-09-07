class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [1,2,3,4,5,6]
        # [3,4,5,6,1,2]

        # Binary Search
        # Number can be in sorted half of rotated half

        if len(nums)==0:
            return -1
        l,r = 0,len(nums)-1

        while l<=r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid

            # if left half is sorted
            if nums[l]<=nums[mid]:
                # number not in this half
                if target>nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target<nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

                
