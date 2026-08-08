class Solution:
    def isValidBST(self, root):
        stack = []
        current = root
        prev = None

        while current or stack:
            # Go left
            while current:
                stack.append(current)
                current = current.left

            # Visit node
            current = stack.pop()

            # Check increasing order
            if prev is not None and current.val <= prev:
                return False

            prev = current.val

            # Go right
            current = current.right

        return True