from collections import defaultdict, deque
import heapq

class Twitter:

    def __init__(self):
        self.followee = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.counter, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft()

        self.counter += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        users = {userId} | self.followee[userId]
        heap = []
        for u in users:
            for t in self.tweets[u]:
                heapq.heappush(heap, t)
                if len(heap) > 10:
                    heapq.heappop(heap)
        
        return [x[1] for x in sorted(heap, reverse=True)]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followee[followerId]:
            self.followee[followerId].remove(followeeId)
