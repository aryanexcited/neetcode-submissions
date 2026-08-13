# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:       
        def check(root: Optional[TreeNode], low: int, high: int) -> bool:
            if not root:
                return True
            
            if not low < root.val < high:
                return False
            
            left = check(root.left,low,root.val)
            right = check(root.right,root.val,high)
            return left and right 
        
        ans = check(root,-math.inf,math.inf)
        return ans