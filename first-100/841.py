from collections import defaultdict
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = self.get_adjacency_list(rooms)
        visited = set()
        self.dfs(graph, 0, visited)

        return len(visited) == len(graph.keys())

    def get_adjacency_list(self, rooms):
        graph = defaultdict(list)

        for i, room in enumerate(rooms):
            graph[i] += room

        return graph

    def dfs(self, graph, cur, visited):
        visited.add(cur)
        neighbors = graph[cur]
        for neighbor in neighbors:
            if neighbor not in visited:
                self.dfs(graph, neighbor, visited)


if __name__ == "__main__":
    s = Solution()
    print(s.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))  # False
    print(s.canVisitAllRooms([[1], [2], [3], []]))  # True
