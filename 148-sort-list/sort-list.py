class Solution:
    def sortList(self, head):
        # Empty list or one node
        if not head or not head.next:
            return head

        # Find the middle of the list
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list into two halves
        mid = slow.next
        slow.next = None

        # Sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge sorted halves
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0)
        current = dummy

        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        # Attach remaining nodes
        if left:
            current.next = left
        else:
            current.next = right

        return dummy.next