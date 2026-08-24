class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Array is sorted but smallest item is not at nums[0]
        # to binary search, we need the index of the smallest nums

        # [4,5,6,7,8,9,10,1,2,3]

        l = 0 
        r = len(nums) - 1 # 9
        while l < r:
            m = (l + r) // 2 # (0 + 9) //2 = 4.5 = 4
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) //2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        result = binary_search(0, pivot - 1)
        if result != -1:
            return result

        return binary_search(pivot, len(nums) - 1)