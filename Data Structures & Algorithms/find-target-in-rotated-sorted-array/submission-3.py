class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Just search lol: O(N)
        # Since it's rotated: Do 2 ptr till the converge on pivot: O(N)

        # [3,4,5,6,1,2]
        
        n = len(nums)
        l,r=0,n-1
        while l<=r:
            mid = (l+r)//2

            if target == nums[mid]:
                return mid

            # if left half is sorted
            if nums[l]<=nums[mid]:
                # but target is in right half
                if target>nums[mid] or target<nums[l]:
                    l = mid+1
                # target is in this half
                else:
                    r = mid - 1
            # if right half is sorted
            else:
                # but target is in the other half
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                # target is in this half
                else:
                    l = mid + 1
        return -1