class Solution:
    def countStudents(self, students, sandwiches):
        count = [0, 0]

        # Count students who want each sandwich type
        for student in students:
            count[student] += 1

        for sandwich in sandwiches:
            if count[sandwich] == 0:
                return count[0] + count[1]

            count[sandwich] -= 1

        return 0