from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.get_adjacency_list(numCourses, prerequisites)
        visited = [0] * numCourses
        order = []

        for course in range(numCourses):
            if visited[course] == 0:
                if self.dfs(graph, course, visited, order) == True:
                    return []

        return order

    def dfs(self, graph, vertex, visited, order):
        visited[vertex] = 1
        neighbors = graph[vertex]

        for neighbor in neighbors:
            if visited[neighbor] == 0:
                if self.dfs(graph, neighbor, visited, order) == True:
                    return True
            elif visited[neighbor] == 1:
                return True

        visited[vertex] = 2
        order.insert(0, vertex)

        return False

    def get_adjacency_list(self, n, edges):
        graph = defaultdict(list)

        for course in range(n):
            graph[course] = []

        for edge_1, edge2 in edges:
            graph[edge2].append(edge_1)

        return graph


if __name__ == "__main__":
    s = Solution()
    print(s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # [0, 2, 1, 3] or [0, 1, 2, 3]
    print(s.findOrder(2, []))  # [0, 1] or [1, 0]
