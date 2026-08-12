# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(root: TreeNode, max_so_far: int) -> None:
            nonlocal ans
            if not root:
                return None
            
            if root.val >= max_so_far:
                max_so_far = root.val
                ans += 1
            
            dfs(root.left, max_so_far)
            dfs(root.right, max_so_far)

        dfs(root, root.val)
        return ans