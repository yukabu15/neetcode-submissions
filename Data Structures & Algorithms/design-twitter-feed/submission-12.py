class Twitter:

    def __init__(self):
        self.time = 0
        self.followers = [set() for i in range(101)]
        self.posts = [[] for _ in range(101)]
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        post_cand = self.posts[userId][:]
        print(userId, self.posts[userId])
        for followeeId in self.followers[userId]:
            post_cand.extend(self.posts[followeeId])
        post_cand.sort(reverse=True)
        return [tweetId for time, tweetId in post_cand[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].discard(followeeId)
        
