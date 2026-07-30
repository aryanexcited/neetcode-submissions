# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next!=None:
            fast,slow = fast.next.next, slow.next
        
        second, slow.next = slow.next, None

        prev, curr = None, second
        
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        second = prev
        first = head

        while first and second:
            nextN = first.next
            first.next = second
            second = second.next
            first = first.next
            first.next = nextN
            first = first.next
            nextN = nextN.next