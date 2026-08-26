class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = 0
        count = 0
        freq = {0: 1}                       # empty prefix, covers subarrays starting at index 0

        for num in nums:
            prefix_sum += num
            if (diff := prefix_sum - k) in freq:    # count before recording, or k=0 counts the empty subarray
                count += freq[diff]
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count