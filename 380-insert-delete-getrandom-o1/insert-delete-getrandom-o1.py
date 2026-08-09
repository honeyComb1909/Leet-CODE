import random


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.index = {}

    def insert(self, val: int) -> bool:

        if val in self.index:
            return False

        self.index[val] = len(self.nums)
        self.nums.append(val)

        return True

    def remove(self, val: int) -> bool:

        if val not in self.index:
            return False

        # Index of the element to remove
        idx = self.index[val]

        # Last element in the list
        last = self.nums[-1]

        # Move last element to the position of val
        self.nums[idx] = last
        self.index[last] = idx

        # Remove last element
        self.nums.pop()
        del self.index[val]

        return True

    def getRandom(self) -> int:

        return random.choice(self.nums)