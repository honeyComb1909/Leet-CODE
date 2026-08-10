from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        # stop -> list of buses containing that stop
        stop_to_buses = defaultdict(list)

        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_to_buses[stop].append(bus)

        queue = deque([(source, 0)])

        visited_stops = {source}
        visited_buses = set()

        while queue:
            stop, buses_taken = queue.popleft()

            for bus in stop_to_buses[stop]:

                # Already used this bus
                if bus in visited_buses:
                    continue

                visited_buses.add(bus)

                for next_stop in routes[bus]:

                    if next_stop == target:
                        return buses_taken + 1

                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append(
                            (next_stop, buses_taken + 1)
                        )

        return -1