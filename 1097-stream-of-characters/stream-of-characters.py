class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class StreamChecker:

    def __init__(self, words: list[str]):
        self.root = TrieNode()
        self.stream = []

        # Insert reversed words into Trie
        for word in words:
            node = self.root

            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

            node.is_word = True

        # Maximum word length
        self.max_len = max(len(word) for word in words)

    def query(self, letter: str) -> bool:

        self.stream.append(letter)

        # Only need to check up to the maximum word length
        node = self.root

        for ch in reversed(self.stream[-self.max_len:]):

            if ch not in node.children:
                return False

            node = node.children[ch]

            if node.is_word:
                return True

        return False