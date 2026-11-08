class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.time = 0
        self.tweets = defaultdict(deque)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        max_h = []
        for u in self.followers[userId] | {userId}:
            for tweet in self.tweets[u]:
                heapq.heappush(max_h, tweet)
        res = []
        while max_h and len(res) < 10:
            res.append(heapq.heappop(max_h)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)    

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)    
        
