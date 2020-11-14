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
