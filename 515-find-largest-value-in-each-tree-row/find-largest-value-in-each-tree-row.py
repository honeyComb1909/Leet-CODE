class Solution:
    def largestValues(self, root):
        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            max_val = float('-inf')
            next_level = []

            for node in queue:
                max_val = max(max_val, node.val)

                if node.left:
                    next_level.append(node.left)

                if node.right:
                    next_level.append(node.right)

            result.append(max_val)
            queue = next_level

        return result