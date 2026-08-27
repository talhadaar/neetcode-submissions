class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort

        # Put numbers in buckets that represent frequencies

        # Count frequencies
        fmap = defaultdict(int)
        for num in nums:
            fmap[num]+=1
        

        n = len(nums)
        buckets = [[] for i in range(n+1)]
        for num,f in fmap.items():
            buckets[f].append(num)

        # check buckets in reverse and find k items
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res