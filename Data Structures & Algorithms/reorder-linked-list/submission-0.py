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
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None

        prev = None
        curr = second
        while curr:
            nextN = curr.next
            curr.next = prev
            prev = curr
            curr = nextN
        
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