from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.followees = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop(0)
        self.count += 1
    
    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for u in self.followees[userId] | {userId}:
            for tweet in self.tweets[u]:
                heapq.heappush(feed, tweet)
                if len(feed) > 10:
                    heapq.heappop(feed)
        return [x[1] for x in sorted(feed, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)
        
