from collections import Counter

class Solution:
    def findFrequentTreeSum(self, root):
        if not root:
            return []

        freq = Counter()

        def dfs(node):
            if not node:
                return 0

            total = node.val + dfs(node.left) + dfs(node.right)
            freq[total] += 1

            return total

        dfs(root)

        max_freq = max(freq.values())

        return [s for s, count in freq.items() if count == max_freq]