# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        idx_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0  

        def build(in_start, in_end):
            if in_start > in_end:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            node = TreeNode(root_val)
            
            mid = idx_map[root_val]
            
            node.left = build(in_start, mid - 1)
            node.right = build(mid + 1, in_end)
            
            return node
        
        return build(0, len(inorder) - 1)