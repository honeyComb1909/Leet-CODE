class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()

        def backtrack(start, current, remaining):

            # Target reached
            if remaining == 0:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):

                # Skip duplicate numbers at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since candidates are sorted
                if candidates[i] > remaining:
                    break

                current.append(candidates[i])

                # i + 1 because each number can be used only once
                backtrack(i + 1, current, remaining - candidates[i])

                # Undo choice
                current.pop()

        backtrack(0, [], target)

        return result