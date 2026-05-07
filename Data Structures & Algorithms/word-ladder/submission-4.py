class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        store = defaultdict(set)
        wordList.append(beginWord)
        q = [beginWord]
        visited = set(q)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                store[pattern].add(word)
        
        res = 1
        while q:
            temp = []
            for word in q:
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for match in store[pattern]:
                        if match not in visited:
                            temp.append(match)
                            visited.add(match)
            q = temp
            res += 1
        
        return 0
        
                    

