class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):

        # Store reserved seats for each affected row
        rows = {}

        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()

            rows[row].add(seat)

        # Every completely empty row can hold 2 families
        answer = (n - len(rows)) * 2

        # Check rows that contain reservations
        for seats in rows.values():

            count = 0

            # Left group: 2,3,4,5
            if all(seat not in seats for seat in [2, 3, 4, 5]):
                count += 1

            # Right group: 6,7,8,9
            if all(seat not in seats for seat in [6, 7, 8, 9]):
                count += 1

            # If left and right aren't both possible,
            # try the middle group: 4,5,6,7
            if count == 0:
                if all(seat not in seats for seat in [4, 5, 6, 7]):
                    count = 1

            answer += count

        return answer