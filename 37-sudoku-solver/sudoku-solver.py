class Solution:
    def solveSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Store existing numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)

        def backtrack():

            # Find the empty cell with the fewest possibilities
            best_cell = None
            best_options = None

            for r in range(9):
                for c in range(9):

                    if board[r][c] == '.':

                        box = (r // 3) * 3 + (c // 3)

                        options = set("123456789") \
                            - rows[r] \
                            - cols[c] \
                            - boxes[box]

                        # No possible number -> dead end
                        if not options:
                            return False

                        # Choose the cell with minimum options
                        if best_options is None or len(options) < len(best_options):
                            best_cell = (r, c)
                            best_options = options

                            # Can't get better than one option
                            if len(options) == 1:
                                break

                if best_options is not None and len(best_options) == 1:
                    break

            # No empty cells -> Sudoku solved
            if best_cell is None:
                return True

            r, c = best_cell
            box = (r // 3) * 3 + (c // 3)

            for num in best_options:

                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

                if backtrack():
                    return True

                # Undo
                board[r][c] = '.'
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box].remove(num)

            return False

        backtrack()