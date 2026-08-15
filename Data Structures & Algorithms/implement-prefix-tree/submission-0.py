class PrefixTree:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def insert(self, word: str) -> None:
        curr = self
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                curr.children[ch] = PrefixTree()
                curr = curr.children[ch]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return False
        return curr.is_end_of_word
        
    def startsWith(self, prefix: str) -> bool:
        curr = self
        for ch in prefix:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return False
        return True