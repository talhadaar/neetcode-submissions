class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Non-descending: ascending with duplicates.
        # Exactly 1 valid solution -> must pick earlier of duplicates

        n = len(numbers)
        l,r=0,n-1

        while l<=r:
            tsum = numbers[r]+numbers[l]
            if tsum == target:
                return [l+1,r+1]
            elif tsum<target:
                l+=1
            else:
                r-=1
