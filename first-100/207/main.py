from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.get_adjacency_list(prerequisites)
        visited = [0] * numCourses

        for course in range(numCourses):
            if visited[course] == 0:
                if self.has_cycle(graph, course, visited) == True:
                    return False

        return True

    def has_cycle(self, graph, vertex, visited):
        visited[vertex] = 1
        neighbors = graph[vertex]

        for neighbor in neighbors:
            if visited[neighbor] == 0:
                if self.has_cycle(graph, neighbor, visited) == True:
                    return True
            elif visited[neighbor] == 1:
                return True

        visited[vertex] = 2

        return False

    def get_adjacency_list(self, edges):
        graph = defaultdict(list)

        for edge1, edge2 in edges:
            graph[edge2].append(edge1)

        return graph


if __name__ == "__main__":
    s = Solution()
    print(s.canFinish(2, [[1, 0]]))  # True
    print(s.canFinish(2, [[1, 0], [0, 1]]))  # False
