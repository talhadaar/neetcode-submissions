class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Brute Force: hashset: add numbers, if one already exists, remove and move one
        # only 1 number is left at the end
        numset = set()
        for num in nums:
            if num in numset:
                numset.remove(num)
                continue
            numset.add(num)
        return numset.pop()
