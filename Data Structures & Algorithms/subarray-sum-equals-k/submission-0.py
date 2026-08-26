class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # prefix[j]-prefix[i] = k <- tells us [i+1,j] is a valid subarray, but we only need occurances
        # We can look for occurances prefix[j]-k = prefix[i]
        res = curSum = 0
        prefixSums = defaultdict(int)
        prefixSums[0] = 1

        for num in nums:
            curSum += num # prefix so far
            res += prefixSums[curSum - k] # if we found a valid prefix[i], increment total
            prefixSums[curSum] += 1 # increment count of the valid prefix[i] we have seen so far

        return res