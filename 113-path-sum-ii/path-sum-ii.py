class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, remaining, path):
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right and remaining == node.val:
                result.append(path.copy())

            dfs(node.left, remaining - node.val, path)
            dfs(node.right, remaining - node.val, path)

            path.pop()

        dfs(root, targetSum, [])
        return result