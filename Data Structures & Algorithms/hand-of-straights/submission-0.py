class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hashMap = Counter(hand)
        print(hashMap)
        heap = []
        for val,freq in hashMap.items():
            heapq.heappush(heap, (val,freq))
        
        while heap:
            while hashMap[heap[0][0]]:
                v = heap[0][0]
                for i in range(groupSize):
                    if hashMap[v+i]:
                        hashMap[v+i] -= 1
                    else:
                        return False

            heapq.heappop(heap)
        return True