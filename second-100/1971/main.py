from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, finish: int) -> bool:
        graph = self.get_adjacency_list(edges)
        visited = [None] * n

        self.dfs(graph, start, visited)

        return visited[finish] == 1

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
    # print(s.get_adjacency_list([[0, 1], [1, 2], [2, 0]]))
    print(s.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))  # True
