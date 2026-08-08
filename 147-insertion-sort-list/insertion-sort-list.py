class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        current = head

        while current:
            next_node = current.next

            # Find the correct position
            prev = dummy

            while prev.next and prev.next.val < current.val:
                prev = prev.next

            # Insert current node
            current.next = prev.next
            prev.next = current

            # Move to the next original node
            current = next_node

        return dummy.next