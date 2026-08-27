class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
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