class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Brute Force: make all subarrays and check sum as k

        # Prefix arrays
        # prefix[j]-prefix[i] = k
        # prefix[j]-k = prefix[i]
        # How many prefix[j]-k have i seen so far?

        # 0:1 because pefix[j]-k can exist for 0'th element
        fmap = defaultdict(int)
        fmap[0]+=1

        count = 0
        pfxSum = 0

        for num in nums:
            pfxSum+=num
            diff = pfxSum - k

            if diff in fmap:
                count += fmap[diff]
            fmap[pfxSum]+=1
        return count