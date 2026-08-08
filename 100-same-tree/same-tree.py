class Solution:
    def isSameTree(self, p, q):
        # Both are empty
        if not p and not q:
            return True

        # One is empty, the other is not
        if not p or not q:
            return False

        # Values are different
        if p.val != q.val:
            return False

        # Check left and right subtrees
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))