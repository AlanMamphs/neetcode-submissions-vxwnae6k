class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp -= 1
        self.tweets[userId].append((self.timestamp, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        m_heap = []
        for user in self.followers[userId] | {userId}:
            for t in self.tweets[user]:
                heapq.heappush(m_heap, t) 
        res = []
        while m_heap and len(res) < 10:
            res.append(heapq.heappop(m_heap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)        
