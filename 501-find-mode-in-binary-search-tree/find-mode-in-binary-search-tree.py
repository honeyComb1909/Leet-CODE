class Solution:
    def findMode(self, root):
        result = []
        prev = None
        count = 0
        max_count = 0

        def inorder(node):
            nonlocal prev, count, max_count

            if not node:
                return

            inorder(node.left)

            if prev == node.val:
                count += 1
            else:
                count = 1

            if count > max_count:
                max_count = count
                result.clear()
                result.append(node.val)
            elif count == max_count:
                result.append(node.val)

            prev = node.val

            inorder(node.right)

        inorder(root)
        return result