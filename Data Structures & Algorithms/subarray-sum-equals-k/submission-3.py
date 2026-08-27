class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Brute Force: make all subarrays and check sum as k

        # Prefix arrays
        # prefix[j]-prefix[i] = k
        # prefix[j]-k = prefix[i]
        # How many prefix[j]-k have i seen so far?

        # 0:1 because pefix[j]-k can exist for 0'th element
        fmap = {0:1}
        n = len(nums)

        currPrefix = 0
        count = 0
        for num in nums:
            currPrefix+=num
            diff = currPrefix - k

            count+= fmap.get(diff,0)
            fmap[currPrefix] = 1 + fmap.get(currPrefix,0)

        return count