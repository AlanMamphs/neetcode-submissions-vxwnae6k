class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        store = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            min_len = min(len(w1), len(w2))
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return ''
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    store[w1[j]].add(w2[j])
                    break
        res = []
        visited = dict()
        
        def dfs(c):
            if c in visited:
                if visited[c]:
                    return 'cycle'
                return 'not-cycle'
            visited[c] = True

            for p in store[c]:
                if dfs(p) == 'cycle':
                    return 'cycle'
            visited[c] = False
            res.append(c)
            return 'not-cycle'

        for c in store:
          if dfs(c) == 'cycle':
            return ''
        return ''.join(res)[::-1]


