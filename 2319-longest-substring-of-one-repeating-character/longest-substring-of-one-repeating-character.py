class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)
        size = 1
        while size < n:
            size <<= 1

        # Each node is one integer:
        # [length | pre | suf | best | left_char | right_char]
        B = 20
        MASK = (1 << B) - 1

        tree = [0] * (2 * size)

        def encode(length, pre, suf, best, lc, rc):
            return (
                (length << 105)
                | (pre << 85)
                | (suf << 65)
                | (best << 45)
                | (lc << 40)
                | (rc << 35)
            )

        def decode(x):
            return (
                x >> 105,
                (x >> 85) & MASK,
                (x >> 65) & MASK,
                (x >> 45) & MASK,
                (x >> 40) & 31,
                (x >> 35) & 31
            )

        for i, c in enumerate(s):
            v = ord(c) - 97
            tree[size + i] = encode(1, 1, 1, 1, v, v)

        def merge(a, b):
            if not a:
                return b
            if not b:
                return a

            la, pa, sa, ba, lca, rca = decode(a)
            lb, pb, sb, bb, lcb, rcb = decode(b)

            pre = pa
            suf = sb
            best = max(ba, bb)

            if rca == lcb:
                best = max(best, sa + pb)

                if pa == la:
                    pre = la + pb

                if sb == lb:
                    suf = sa + lb

            return encode(
                la + lb,
                pre,
                suf,
                best,
                lca,
                rcb
            )

        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[i << 1], tree[i << 1 | 1])

        ans = []

        for idx, ch in zip(queryIndices, queryCharacters):
            p = size + idx
            v = ord(ch) - 97
            tree[p] = encode(1, 1, 1, 1, v, v)

            p >>= 1
            while p:
                tree[p] = merge(tree[p << 1], tree[p << 1 | 1])
                p >>= 1

            ans.append((tree[1] >> 45) & MASK)

        return ans