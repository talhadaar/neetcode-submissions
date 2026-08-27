class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute: Sort and count

        # Count frequencies and return the top K elements.

        # A. count frequencies
        # B. A ds that can give me top k freq elements(max heap)

        # Count frequencies, heapify them, then pop the top k ones.

        fmap = defaultdict(int)
        for num in nums:
            fmap[num]+=1

        heap = []
        for num in fmap.keys():
            heapq.heappush(heap, (fmap[num], num))
            if len(heap)>k:
                heapq.heappop(heap)


        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res