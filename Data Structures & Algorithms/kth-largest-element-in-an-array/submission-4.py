class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        n = len(nums)
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif heap and heap[0] < num:
                heapq.heappush(heap,num)
                heapq.heappop(heap)
        
        return heap[0]