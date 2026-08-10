from collections import deque, Counter

class Solution:
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        n = len(friends)

        visited = [False] * n
        visited[id] = True

        queue = deque([id])

        current_level = 0
        target_friends = []

        while queue:
            size = len(queue)

            for _ in range(size):
                person = queue.popleft()

                if current_level == level:
                    target_friends.append(person)
                    continue

                for friend in friends[person]:
                    if not visited[friend]:
                        visited[friend] = True
                        queue.append(friend)

            if current_level == level:
                break

            current_level += 1

        # Count videos
        frequency = Counter()

        for person in target_friends:
            for video in watchedVideos[person]:
                frequency[video] += 1

        # Sort by frequency, then alphabetically
        return sorted(frequency, key=lambda x: (frequency[x], x))