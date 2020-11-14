# https://leetcode.com/problems/course-schedule/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = {}

        for i in range(numCourses):
            in_degree[i] = set()

        for pre in prerequisites:
            chil, par = pre
            in_degree[chil].add(par)

        queue = collections.deque([])
        for node in in_degree:
            if len(in_degree[node]) == 0:
                queue.append(node)

        if not queue:
            return False

        while queue:
            node = queue.popleft()
            del in_degree[node]
            for vertex in in_degree:
                if node in in_degree[vertex]:
                    in_degree[vertex].remove(node)
                    if len(in_degree[vertex]) == 0:
                        queue.append(vertex)

        for node in in_degree:
            if len(in_degree[node]) != 0:
                return False

        return True

