class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        n3 = n // 3

        # Brutus: sort and count. Space: O(1), compute: O(n) depending on sorting algo.
        # FreqMap and FreqArray will take too much space to initialize
        nums.sort()
        res = []
        i = 0
        while i < n:
            count = 1
            while i<n-1 and nums[i] == nums[i+1]:
                i+=1
                count+=1
            if count > n3:
                res.append(nums[i])
            i+=1

        return res