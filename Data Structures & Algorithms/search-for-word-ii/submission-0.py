class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False
    
    def add_word(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isword = True
    
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add_word(word)

        R, C = len(board), len(board[0])
        visit, res = set(), set()

        def dfs(r, c, node, prefix):
            if (
                r not in range(R)
                or c not in range(C)
                or (r, c) in visit
                or board[r][c] not in node.children
            ):
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            prefix += board[r][c]
            if node.isword:
                res.add(prefix)
            
            for i, j in DIRECTIONS:
                dfs(r + i, c + j, node, prefix)
            visit.remove((r, c))
            

        for r in range(R):
            for c in range(C):
                dfs(r, c, root, "")
        
        return list(res)
