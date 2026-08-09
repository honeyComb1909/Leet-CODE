class Solution:
    def exclusiveTime(self, n, logs):
        stack = []
        result = [0] * n
        prev_time = 0

        for log in logs:
            func_id, action, time = log.split(":")
            func_id = int(func_id)
            time = int(time)

            if action == "start":
                # Current function gets the time
                # from prev_time up to time - 1
                if stack:
                    result[stack[-1]] += time - prev_time

                stack.append(func_id)
                prev_time = time

            else:
                # End time is inclusive
                result[stack[-1]] += time - prev_time + 1

                stack.pop()

                # Next execution starts after this timestamp
                prev_time = time + 1

        return result