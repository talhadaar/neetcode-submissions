class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1 <= nums <= n
        # len(nums)==n+1
        # Exactly 1 duplicate
        # [5,6,3,6,1,2]

        # Sorting the finding adjacent dupes- O(n*SORTING) and O(SORTING)
        # HashSet(or Array of size n+1): O(n) and O(n)
        
        
        # Negative Marking: If nums[nums[i]]*-1 to mark a num as seen, if nums[nums[i]] already -, we found nums[i] as duplicate
        # Works because: 

        for num in nums:
            idx = abs(num)
            if nums[idx] < 0:
                return abs(num)
            nums[idx]*=-1
        return -1