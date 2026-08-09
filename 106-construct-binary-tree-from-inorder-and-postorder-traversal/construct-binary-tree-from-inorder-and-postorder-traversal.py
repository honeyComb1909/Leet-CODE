class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        # Last element in postorder is the root
        root_val = postorder.pop()
        root = TreeNode(root_val)

        # Find root in inorder
        root_index = inorder.index(root_val)

        # Important:
        # Build RIGHT first because we are removing
        # elements from the end of postorder.
        root.right = self.buildTree(inorder[root_index + 1:], postorder)
        root.left = self.buildTree(inorder[:root_index], postorder)

        return root