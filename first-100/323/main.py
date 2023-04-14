from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = self.get_adjacency_list(edges)
        visited = [None] * n
        counter = 0

        for vertex in graph:
            if not visited[vertex]:
                counter += 1
                self.dfs(graph, vertex, visited)

        return counter

    def dfs(self, graph, vertex, visited):
        visited[vertex] = 1
        neighbors = graph[vertex]

        for neighbor in neighbors:
            if not visited[neighbor]:
                self.dfs(graph, neighbor, visited)

    def get_adjacency_list(self, edges):
        graph = defaultdict(list)

        for edge_1, edge_2 in edges:
            graph[edge_1].append(edge_2)
            graph[edge_2].append(edge_1)

        return graph


if __name__ == "__main__":
    s = Solution()
    print(s.countComponents(5, [[0, 1], [1, 2], [3, 4]]))  # 2
