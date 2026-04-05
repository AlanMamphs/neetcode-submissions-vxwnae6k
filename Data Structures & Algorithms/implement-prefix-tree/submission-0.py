class Node:
    def __init__(self):
        self.key = None
        self.children = dict()
        self.isword = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.isword = True
    
    def _get(self, word):
        curr = self.root
        for c in word:
            curr = curr.children.get(c)
            if not curr:
                break
        return curr

    def search(self, word: str) -> bool:
        node = self._get(word)
        return bool(node) and node.isword

    def startsWith(self, prefix: str) -> bool:
        node = self._get(prefix)
        return bool(node)
        