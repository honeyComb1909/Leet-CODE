class Solution:
    def findTilt(self, root):
        total_tilt = 0

        def dfs(node):
            nonlocal total_tilt

            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            total_tilt += abs(left_sum - right_sum)

            return left_sum + right_sum + node.val

        dfs(root)
        return total_tilt