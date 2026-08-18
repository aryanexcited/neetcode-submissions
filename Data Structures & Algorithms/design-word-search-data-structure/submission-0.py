class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False        

    def addWord(self, word: str) -> None:
        curr = self
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                curr.children[ch] = WordDictionary()
                curr = curr.children[ch]
        curr.is_end_of_word=True
        
    def search(self, word: str) -> bool:
        curr = self
        index = 0
        def dfs(node, index):
            if index == len(word):
                return node.is_end_of_word
            
            if word[index]!='.':
                if word[index] not in node.children:
                    return False
                else:
                    return dfs(node.children[word[index]], index+1)
            else:
                return any (dfs(child, index+1) for child in node.children.values())
        
        return dfs(curr,index)