class Twitter:
    # Things to track: userID, tweetID, feed, following
    def __init__(self):
        self.userBase = {}
        self.tweets = collections.deque()

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userBase:
            self.userBase[userId] = set([userId])
        self.tweets.appendleft((userId, tweetId))

            

    def getNewsFeed(self, userId: int) -> List[int]:
        following = set(self.userBase[userId])
        res=collections.deque()
        for tweet in self.tweets:
            if len(res)>9:   
                break
            if tweet[0] in following:
                res.append(tweet[1])
        return list(res)
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userBase:
            self.userBase[followerId] = set([followeeId])
        else:
            self.userBase[followerId].add(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userBase[followerId] and followeeId != followerId:
            self.userBase[followerId].remove(followeeId)
        
        
