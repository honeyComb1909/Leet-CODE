class Solution:
    def friendRequests(self, n, restrictions, requests):
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            a = find(a)
            b = find(b)

            if a == b:
                return

            if size[a] < size[b]:
                a, b = b, a

            parent[b] = a
            size[a] += size[b]

        ans = []

        for u, v in requests:
            ru = find(u)
            rv = find(v)

            # Already friends
            if ru == rv:
                ans.append(True)
                continue

            allowed = True

            # Check every restriction
            for x, y in restrictions:
                rx = find(x)
                ry = find(y)

                # After merging ru and rv, x and y would
                # become friends -> request is forbidden.
                if (rx == ru and ry == rv) or \
                   (rx == rv and ry == ru):
                    allowed = False
                    break

            if allowed:
                union(ru, rv)
                ans.append(True)
            else:
                ans.append(False)

        return ans