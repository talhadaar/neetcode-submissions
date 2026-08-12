class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Count frequencies
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Heapify 
        # Sorted by count
        # heap[count][key]
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            # we only want top k, so keep popping the smaller ones
            # leaving only largest 3
            if len(heap)>k:
                heapq.heappop(heap)
            
        # take top k elements from heap
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res