class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [0,1,1,2] everything after 0's is 1 and everything after 1s is 2

        # [2,2,1,0,2,1,0,0,1]
        # [0,0,1,1,2,1,0,2,2]
        
        # Counting sort - Count the digits then place that many in required order

        # 1s in middle, 0s and 2s to its right
        # so move 0s to the rightmost left position
        # 2s to leftmost right available position
        # swapping 2 could've bright a 0 or 1 in incorrect position, so we need to step back and reevaluate
        l,r = 0, len(nums) - 1
        i = 0

        def swap(i,j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j]=tmp

        while i<=r:
            if nums[i] == 0:
                swap(i,l)
                l+=1
            elif nums[i] == 2:
                swap(i,r)
                r-=1
                continue
            i+=1
