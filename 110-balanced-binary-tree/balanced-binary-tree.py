class Solution:
    def isBalanced(self, root):

        def height(node):

            # Empty tree has height 0
            if not node:
                return 0

            # Get left subtree height
            left = height(node.left)

            # Get right subtree height
            right = height(node.right)

            # If either subtree is unbalanced
            if left == -1 or right == -1:
                return -1

            # Current node is unbalanced
            if abs(left - right) > 1:
                return -1

            # Return height of current subtree
            return 1 + max(left, right)

        return height(root) != -1