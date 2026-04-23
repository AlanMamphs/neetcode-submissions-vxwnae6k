class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        store = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                store[pattern].append(word)
            
        q = deque([beginWord])
        visited = set([beginWord])
        count = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neighbor in store[pattern]:
                        if neighbor in visited:
                            continue
                        q.append(neighbor)
                        visited.add(neighbor)
            count += 1
        return 0