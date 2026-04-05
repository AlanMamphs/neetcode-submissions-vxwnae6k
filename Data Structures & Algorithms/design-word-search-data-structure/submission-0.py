class Node:
    def __init__(self):
        self.children = dict()
        self.isword = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.isword = True

    def search(self, word: str) -> bool:
        curr = self.root
        stack = [(curr, 0)]
        while stack:
            curr, i = stack.pop()
            if i == len(word) and curr.isword:
                return True
            if i == len(word):
                continue
            c = word[i]
            if c in curr.children:
                stack.append((curr.children[c], i + 1))
            elif c == '.':
                stack.extend((v, i + 1) for v in curr.children.values())
        return False








