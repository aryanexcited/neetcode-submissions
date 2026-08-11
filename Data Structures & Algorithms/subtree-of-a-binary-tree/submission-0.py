# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p and q or p and not q:
                return False
            leftSub = isSameTree(p.left,q.left)
            rightSub = isSameTree(p.right,q.right)
            return leftSub and rightSub and p.val == q.val   
         
        if isSameTree(root,subRoot):
            return True

        leftCheck = self.isSubtree(root.left,subRoot)
        rightCheck = self.isSubtree(root.right,subRoot)
        return True if (leftCheck or rightCheck) else False
