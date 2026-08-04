# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        result = ListNode()
        headR = result
        counter = 1
        for head in lists:
            if head:
                heapq.heappush(heap,(head.val,counter,head))
                counter += 1
        
        while heap:
            popped_item = heapq.heappop(heap)
            result.next = popped_item[2]
            if result.next.next:
                counter += 1
                heapq.heappush(heap,(popped_item[2].next.val,counter,popped_item[2].next))
            result = result.next
            result.next = None

        
        return headR.next
