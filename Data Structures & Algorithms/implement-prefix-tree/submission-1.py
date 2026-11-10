class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.end = False

class PrefixTree:

    def __init__(self):
        self.data = Node()

    def insert(self, word: str) -> None:
        curr = self.data
        for c in word:
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.data
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end


    def startsWith(self, prefix: str) -> bool:
        curr = self.data
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

        