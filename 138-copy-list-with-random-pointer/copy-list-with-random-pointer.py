class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # Map original node → copied node
        old_to_new = {}

        current = head

        # Create copies of all nodes
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # Connect next and random pointers
        current = head

        while current:
            old_to_new[current].next = old_to_new.get(current.next)
            old_to_new[current].random = old_to_new.get(current.random)

            current = current.next

        return old_to_new[head]