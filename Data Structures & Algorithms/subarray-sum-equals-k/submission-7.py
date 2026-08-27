class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = count = 0
        freq = {0: 1}                          # the empty prefix, seen once

        for num in nums:
            curSum += num
            if (diff := curSum - k) in freq:   # look up BEFORE recording curSum
                count += freq[diff]
            freq[curSum] = freq.get(curSum, 0) + 1

        return count