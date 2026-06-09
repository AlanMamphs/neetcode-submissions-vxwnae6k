class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: [] for w in words for c in w}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            min_len = min(len(w1), len(w2))

            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return ''
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break
        
        res = []
        visited = dict()
        def dfs(c):
            if c in visited:
                if visited[c]:
                    return False
                return True
            visited[c] = True

            for p in adj[c]:
                if not dfs(p):
                    return False
                
            visited[c] = False
            res.append(c)

            return True

        for c in adj:
            if not dfs(c):
                return ''
        return ''.join(res[::-1])