class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        visited = set()

        R = len(board)
        C = len(board[0])

        dictionary = TrieNode()

        for word in words:
            curr = dictionary
            for c in word:
                curr = curr.children[c]
            curr.end = True

        res = set()
        def dfs(root, r, c, prefix):
            if r not in range(R) or c not in range(C) or (r, c) in visited:
                return False
            if board[r][c] not in root.children:
                return False
            visited.add((r, c))
            node = root.children[board[r][c]]
            prefix += board[r][c]
            if node.end:
                res.add(prefix)
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(node, r + dr, c + dc, prefix)
            visited.remove((r, c))
       
        for r in range(R):
            for c in range(C):
                dfs(dictionary, r, c, '')
        
        return list(res)