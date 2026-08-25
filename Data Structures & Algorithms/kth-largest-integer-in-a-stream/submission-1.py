class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            if len(self.heap) > k:
                heapq.heappop(self.heap)
            heapq.heappush(self.heap,num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]