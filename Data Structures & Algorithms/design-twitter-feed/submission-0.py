class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        candidates = self.following[userId].copy()
        candidates.add(userId)
        
        heap = []

        for candidate in candidates:
            n = len(self.tweets[candidate])
            if n > 0:
                heapq.heappush(heap, (-self.tweets[candidate][n-1][0],candidate,n-1))

        feed = []
        for _ in range(10):
            if not heap:
                break
            _,candidate,index = heapq.heappop(heap)
            feed.append(self.tweets[candidate][index][1])
            if index > 0 and self.tweets[candidate][index-1]:
                heapq.heappush(heap,(-self.tweets[candidate][index-1][0],candidate,index-1))
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)