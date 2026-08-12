class Solution:
    def findBottomLeftValue(self, root):
        queue = [root]

        while queue:
            node = queue.pop(0)

            if node.right:
                queue.append(node.right)

            if node.left:
                queue.append(node.left)

        return node.val