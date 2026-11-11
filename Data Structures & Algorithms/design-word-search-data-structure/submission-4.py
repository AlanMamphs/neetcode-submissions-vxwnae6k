class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False

class WordDictionary:

    def __init__(self):
        self.data = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.data
        for c in word:
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if not node:
                return False
            if i == len(word):
                return node.end
            for key, child in node.children.items():
                if word[i] in (key, '.') and dfs(child, i + 1):
                    return True
            return False
        return dfs(self.data, 0)