class Node:
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        # Dummy head and tail
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        # key -> Node
        self.key_node = {}

    def _insert_after(self, prev_node, new_node):
        new_node.next = prev_node.next
        new_node.prev = prev_node

        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:

        # New key
        if key not in self.key_node:

            # Need a count-1 node
            if self.head.next != self.tail and self.head.next.count == 1:
                node = self.head.next
            else:
                node = Node(1)
                self._insert_after(self.head, node)

            node.keys.add(key)
            self.key_node[key] = node

            return

        # Existing key
        current = self.key_node[key]
        new_count = current.count + 1

        # If next node already has new count
        if current.next != self.tail and current.next.count == new_count:
            next_node = current.next
        else:
            next_node = Node(new_count)
            self._insert_after(current, next_node)

        # Move key
        current.keys.remove(key)
        next_node.keys.add(key)

        self.key_node[key] = next_node

        # Remove empty node
        if not current.keys:
            self._remove_node(current)

    def dec(self, key: str) -> None:

        current = self.key_node[key]

        # Count becomes zero
        if current.count == 1:

            del self.key_node[key]
            current.keys.remove(key)

            if not current.keys:
                self._remove_node(current)

            return

        new_count = current.count - 1

        # Previous node already has new count
        if current.prev != self.head and current.prev.count == new_count:
            prev_node = current.prev
        else:
            prev_node = Node(new_count)
            self._insert_after(current.prev, prev_node)

        # Move key
        current.keys.remove(key)
        prev_node.keys.add(key)

        self.key_node[key] = prev_node

        # Remove empty node
        if not current.keys:
            self._remove_node(current)

    def getMaxKey(self) -> str:

        if self.tail.prev == self.head:
            return ""

        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:

        if self.head.next == self.tail:
            return ""

        return next(iter(self.head.next.keys))