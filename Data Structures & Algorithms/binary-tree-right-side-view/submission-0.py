# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        ans = list()
        while queue:
            temp = 0
            length = len(queue)
            while length:
                item = queue.popleft()
                length -= 1
                if item:
                    temp = item.val
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            ans.append(temp)
        return ans