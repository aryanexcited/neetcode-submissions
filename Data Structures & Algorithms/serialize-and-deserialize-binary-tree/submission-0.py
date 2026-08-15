# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = ""
        queue = deque()
        queue.append(root)
        while queue:
            popI = queue.popleft()
            if popI is None:
                ans += "null" + ","
            else:
                ans += str(popI.val) + ","
                queue.append(popI.left)
                queue.append(popI.right)
        return ans

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        valueArr = data.split(",")
        n = len(valueArr)
        queue = deque()
        if valueArr[0] == 'null':
            return None
        head = TreeNode(int(valueArr[0]))
        queue.append(head)
        i = 1
        while i < n and queue:
            node = queue.popleft()
            if valueArr[i] == 'null':
                node.left = None
            else:
                node.left = TreeNode(int(valueArr[i]))
            if valueArr[i+1] == 'null':
                node.right = None
            else:
                node.right = TreeNode(int(valueArr[i+1]))
            i += 2
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return head