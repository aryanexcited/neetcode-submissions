"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        keyMap = defaultdict()
        dummy = head

        while dummy:
            copy_node = Node(dummy.val)
            keyMap[dummy] = copy_node
            dummy = dummy.next

        dummy = head
        result = Node(0)
        headR = result
        while dummy:
            result.next = keyMap[dummy]
            result = result.next
            result.random = keyMap[dummy.random] if dummy.random else None
            dummy = dummy.next
            result.next = None

        return headR.next
            