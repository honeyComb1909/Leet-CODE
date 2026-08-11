class Codec:

    def serialize(self, root):
        if root is None:
            return ""

        result = []

        def preorder(node):
            if node is None:
                return
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None

        values = list(map(int, data.split(",")))
        index = 0

        def build(low, high):
            nonlocal index

            if index == len(values):
                return None

            val = values[index]

            if val < low or val > high:
                return None

            index += 1

            node = TreeNode(val)
            node.left = build(low, val)
            node.right = build(val, high)

            return node

        return build(float("-inf"), float("inf"))