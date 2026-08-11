class Solution:
    def sortedListToBST(self, head):

        if not head:
            return None

        # Find middle
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow is middle
        root = TreeNode(slow.val)

        # Break the list
        if prev:
            prev.next = None
        else:
            # Only one node
            return root

        # Left half
        root.left = self.sortedListToBST(head)

        # Right half
        root.right = self.sortedListToBST(slow.next)

        return root