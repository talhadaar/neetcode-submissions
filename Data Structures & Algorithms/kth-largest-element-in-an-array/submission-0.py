class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Heap of size k
        # Keep k elements in heap only, processing the entire nums array

        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap)>k:
                heapq.heappop(heap)

        return heap[0]