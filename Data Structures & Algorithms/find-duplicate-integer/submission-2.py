class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1 <= nums <= n
        # len(nums)==n+1
        # Exactly 1 duplicate
        # [5,6,3,6,1,2]

        # Sorting the finding adjacent dupes- O(n*SORTING) and O(SORTING)
        # HashSet(or Array of size n+1): O(n) and O(n)
        
        
        # Negative Marking: If nums[nums[i]]*-1 to mark a num as seen, if nums[nums[i]] already -, we found nums[i] as duplicate
        # woks because of constraints provided
        # O(n), O(1)


        # Fast and Slow ptr - Floyd's Algo
        # Think of it as LL with a cycle
        # Find the cycle, the find the dupe for that cycle

        slow,fast = 0,0
        while True:
            slow = nums[slow] # 1 step
            fast = nums[nums[fast]] # 2 steps
            if slow == fast: 
                # found the intersection of the cycle so with slow ptr
                break

        # now locate the index of the duplicate number
        # slow points to start of the cycle
        ptr = 0
        while True:
            slow = nums[slow]
            ptr = nums[ptr]

            if slow == ptr:
                return slow