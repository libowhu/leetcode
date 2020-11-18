# https://leetcode.com/problems/reconstruct-itinerary/
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        iaka = set()
        for ticket in tickets:
            iaka.add(ticket[0])
            iaka.add(ticket[1])

        graph = {i: [] for i in iaka}

        for ticket in tickets:
            f, t = ticket
            graph[f].append(t)

        for v in graph:
            if len(graph[v]) != 0:
                graph[v].sort()

        def helper(graph, start, temp, output, count):
            if len(temp) == count:
                output.append(temp.copy())
                return

            for idx, vertex in enumerate(graph[start]):
                graph[start].remove(vertex)
                temp.append(vertex)
                helper(graph, vertex, temp, output, count)
                if len(output) == 1:
                    return
                temp.pop()
                graph[start].insert(idx, vertex)

            return False

        output = []
        temp = ['JFK']
        start = 'JFK'
        helper(graph, start, temp, output, len(tickets) + 1)
        return output[0]
