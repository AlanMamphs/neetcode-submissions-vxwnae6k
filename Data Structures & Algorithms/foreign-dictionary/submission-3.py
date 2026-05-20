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
        res = dict()
        visited = set()
        
        def dfs(c):
          if c in visited:
            return False
          if not store[c]:
            res[c] = True
            return True
          
          visited.add(c)

          for p in store[c]:
            if not dfs(p):
              return False
          visited.remove(c)
          store[c] = []
          res[c] = True
          return True

        for c in store:
          if not dfs(c):
            return ''
        return ''.join(res.keys())[::-1]


