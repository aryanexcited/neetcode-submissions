class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap,-stone)
        
        while len(heap) > 1:
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)
            diff = a-b
            if diff > 0:
                heapq.heappush(heap,-diff)
        
        return 0 if not heap else -heap[0]