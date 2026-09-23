class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks)
        heap = [-freq for freq in frequencies.values()]
        heapq.heapify(heap)
        q = deque()

        time = 0
        while q or heap:
            time+=1
            if not heap:
                time = q[0][1]
            else:
                count = heapq.heappop(heap)
                count = 1 + count
                if count:
                    q.append((count, time+n))
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time