class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        fmap = defaultdict(int)
        fmap[0]=1

        j = 0
        res = 0

        for num in nums:
            j = j+num

            i = j - k
            res += fmap[i]
            fmap[j]+=1
        return res