class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return

        if self.size[a] < self.size[b]:
            a, b = b, a

        self.parent[b] = a
        self.size[a] += self.size[b]


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        max_num = max(nums)

        dsu = DSU(max_num + 1)

        # prime factorization
        def get_factors(x):
            factors = []

            d = 2

            while d * d <= x:
                if x % d == 0:
                    factors.append(d)

                    while x % d == 0:
                        x //= d

                d += 1

            if x > 1:
                factors.append(x)

            return factors

        # Connect each number with its prime factors
        for num in nums:
            factors = get_factors(num)

            for factor in factors:
                dsu.union(num, factor)

        # Count numbers in each component
        count = {}

        for num in nums:
            root = dsu.find(num)
            count[root] = count.get(root, 0) + 1

        return max(count.values())