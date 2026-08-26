class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for point in points:
            distance = point[0]**2 + point[1]**2
            heapq.heappush(heap,(-distance,point))
            while heap and len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        for items in heap:
            ans.append(items[1])
        
        return ans