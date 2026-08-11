class Solution:
    def flatten(self, root):
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        right = root.right

        root.right = root.left
        root.left = None

        current = root
        while current.right:
            current = current.right

        current.right = right