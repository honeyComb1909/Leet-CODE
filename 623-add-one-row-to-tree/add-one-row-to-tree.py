class Solution:
    def addOneRow(self, root, val, depth):
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        def dfs(node, d):
            if not node:
                return

            if d == depth - 1:
                left = node.left
                right = node.right

                node.left = TreeNode(val)
                node.left.left = left

                node.right = TreeNode(val)
                node.right.right = right

                return

            dfs(node.left, d + 1)
            dfs(node.right, d + 1)

        dfs(root, 1)
        return root