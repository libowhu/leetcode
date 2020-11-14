# https://leetcode.com/problems/course-schedule-ii/
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = {}

        for i in range(numCourses):
            in_degree[i] = set()

        for pre in prerequisites:
            in_degree[pre[0]].add(pre[1])

        queue = collections.deque([])

        for vertex in in_degree:
            if len(in_degree[vertex]) == 0:
                queue.append(vertex)

        if not queue: return []

        output = []
        while queue:
            vertex = queue.popleft()
            output.append(vertex)
            del in_degree[vertex]
            for v in in_degree:
                if vertex in in_degree[v]:
                    in_degree[v].remove(vertex)
                    if len(in_degree[v]) == 0:
                        queue.append(v)

        return output if len(output) == numCourses else []


#Output all paths
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: set() for i in range(numCourses)}
        degree = {i: 0 for i in range(numCourses)}

        for pre in prerequisites:
            chil, par = pre
            graph[chil].add(par)
            degree[chil] += 1

        queue = collections.deque([])

        for v in degree:
            if degree[v] == 0:
                queue.append(v)

        if not queue: return []

        def backtracking(starts, temp, output):
            if not starts:
                if len(temp) == numCourses:
                    output.append(temp.copy())
                return

            for start in starts:
                temp.append(start)
                new_starts = collections.deque(starts)
                new_starts.remove(start)
                for vertex in graph:
                    if start in graph[vertex]:
                        degree[vertex] -= 1
                        if degree[vertex] == 0:
                            new_starts.append(vertex)

                backtracking(new_starts, temp, output)
                temp.pop()

                for vertex in graph:
                    if start in graph[vertex]:
                        degree[vertex] += 1

        result = []
        backtracking(queue, [], result)
        return result