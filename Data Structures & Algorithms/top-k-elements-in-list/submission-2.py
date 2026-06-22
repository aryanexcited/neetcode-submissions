class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1
        
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (-count, num))

        res = []
        for _ in range(k):
            count, num = heapq.heappop(heap)
            res.append(num)
            
        return res