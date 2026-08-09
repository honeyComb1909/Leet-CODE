import heapq


class Twitter:

    def __init__(self):
        self.time = 0

        # userId -> list of (time, tweetId)
        self.tweets = {}

        # userId -> set of followees
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))

        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:

        # Users whose tweets we need to consider
        users = self.following.get(userId, set()).copy()
        users.add(userId)

        heap = []

        # Put the latest tweet of every relevant user
        for user in users:

            if user in self.tweets and self.tweets[user]:

                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        result = []

        # Get at most 10 most recent tweets
        while heap and len(result) < 10:

            time, tweetId, user, index = heapq.heappop(heap)

            result.append(tweetId)

            # Move to the previous tweet of this user
            index -= 1

            if index >= 0:

                next_time, next_tweetId = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-next_time, next_tweetId, user, index)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId in self.following:
            self.following[followerId].discard(followeeId)