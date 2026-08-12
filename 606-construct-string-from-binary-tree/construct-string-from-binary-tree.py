class Solution:
    def tree2str(self, root):
        if root is None:
            return ""

        def dfs(node):
            if node is None:
                return ""

            s = str(node.val)

            if node.left or node.right:
                s += "(" + dfs(node.left) + ")"

            if node.right:
                s += "(" + dfs(node.right) + ")"

            return s

        return dfs(root)