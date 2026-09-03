class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(queries)
        res = [-1]*n
        intervals.sort()

        query_list = [(key,i) for i,key in enumerate(queries)]
        query_list.sort()

        heap = []
        i = 0
        for query,j in query_list:
            while i < len(intervals) and intervals[i][0] <= query:
                item = intervals[i]
                i += 1
                distance = item[1] - item[0] + 1
                heapq.heappush(heap,(distance,item))

            while heap and heap[0][1][1] < query:
                heapq.heappop(heap)
                
            if heap:
                res[j] = heap[0][0]  

        return res