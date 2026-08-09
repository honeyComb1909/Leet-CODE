class Solution:
    def timeRequiredToBuy(self, tickets, k):
        time = 0
        target = tickets[k]

        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], target)
            else:
                time += min(tickets[i], target - 1)

        return time