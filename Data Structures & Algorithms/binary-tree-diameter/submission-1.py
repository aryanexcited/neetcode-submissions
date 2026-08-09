# Definition for a binary tree root.
# class Treeroot:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diTracker = 0

        def height(root):
            nonlocal diTracker
            if not root:
                return 0
            heightLeft = height(root.left)
            heightRight = height(root.right)
            diTracker = max(diTracker, heightLeft+heightRight)
            return 1 + max(heightRight,heightLeft)
        
        height(root)
        return diTracker