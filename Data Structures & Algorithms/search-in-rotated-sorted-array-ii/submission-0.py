class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Some portion of array is always sorted
        # Do binary search in sorted portion
        # if range is not valid: Move one ptr up or down to reach a valid range
        l,r=0,len(nums)-1
        
        while l<=r:
            mid = l + (r-l) // 2

            # if number is found - return
            if nums[mid] == target:
                return True
            
            # If valid non-descending range
            # do normal binary search
            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # If Invalid Descending range:
            elif nums[l] > nums[mid]:
                # If right half is sorted, search there
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    # if right half not sorted, 
                    r = mid -1
            else:
                # l == mid, just move up
                l+=1

        return False
