class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class Trie:
            def __init__(self):
                self.children = {}
                self.is_end_of_word = False
            
            def addWord(self, word):
                curr = self
                for ch in word:
                    if ch in curr.children:
                        curr = curr.children[ch]
                    else:
                        curr.children[ch] = Trie()
                        curr = curr.children[ch]
                
                curr.is_end_of_word = True
            
        trie = Trie()
        for word in words:
            trie.addWord(word)
        
        res = []
        n = len(board)-1
        m = len(board[0])-1
        def dfs(row, col, node, path):
            if not (0<=row<=n and 0<=col<=m) or (board[row][col] not in node.children) or board[row][col] == "#":
                        return False

            char = board[row][col]
            path += char
            if node.children[char].is_end_of_word:
                res.append("".join(path))
                node.children[char].is_end_of_word = False
            
            board[row][col] = "#"
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(row+dr, col+dc, node.children[char], path)   
            
            board[row][col] = char

        for row in range(n+1):
            for col in range(m+1):
                dfs(row,col,trie,"")
        
        return res