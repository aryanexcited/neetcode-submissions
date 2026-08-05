# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = head
        prev = ListNode()
        prev.next = dummy
        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            if (head == None or head.next == None):
                return head
            
            newHead = reverseList(head.next)
            head.next.next = head
            head.next = None
            return newHead

        def findKth_node(head: Optional[ListNode], k: int) -> Optional[ListNode]:
            k -= 1
            while k>0:
                if head.next == None:
                    return None
                head = head.next
                k -= 1
            return head
        
        while dummy:
            kth_Node = findKth_node(dummy,k)
            if kth_Node == None:
                if prev!=None:
                    prev.next = dummy
                break
            nextGroup = kth_Node.next
            kth_Node.next = None
            reverseList(dummy)
            if dummy == head:
                head = kth_Node
            else:
                prev.next = kth_Node
            prev = dummy
            dummy = nextGroup
            
            
        return head