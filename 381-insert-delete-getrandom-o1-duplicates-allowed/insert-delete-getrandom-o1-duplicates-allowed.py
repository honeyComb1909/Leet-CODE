import random
from collections import defaultdict


class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.indices = defaultdict(set)

    def insert(self, val: int) -> bool:

        # Check whether val already exists
        is_new = val not in self.indices or len(self.indices[val]) == 0

        # Add value to the list
        self.nums.append(val)

        # Store its index
        self.indices[val].add(len(self.nums) - 1)

        return is_new

    def remove(self, val: int) -> bool:

        if val not in self.indices or not self.indices[val]:
            return False

        # Get any index containing val
        idx = self.indices[val].pop()

        # Get the last element
        last = self.nums[-1]

        # Move last element to idx
        self.nums[idx] = last

        # Remove last element from list
        self.nums.pop()

        # Update the index set of last
        if idx != len(self.nums):
            self.indices[last].remove(len(self.nums))
            self.indices[last].add(idx)

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)