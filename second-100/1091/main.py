from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, graph: List[List[int]]) -> int:
        distance = [None] * len(graph)
        NOT_VISITED, VISITED = 0, 1
        visited = [NOT_VISITED] * len(graph)
        queue = deque()
        start = 0

        distance[start] = 0
        visited[start] = VISITED
        queue.append(start)

        while len(queue):
            # извлекаем вершину, которую будем обрабатывать
            cur = queue.popleft()
            # print(cur, end=" ")
            # visited.add(cur)

            # соседи этой вершины
            neighbors = graph[cur]
            for neighbor in range(len(neighbors)):
                # если сосед еще не посещен
                if visited[neighbor] == NOT_VISITED:
                    visited[neighbor] = VISITED  # помечаем его как посещенного
                    distance[neighbor] = distance[cur] + 1  # его расстояние на 1 больше расстояния до текущей вершины
                    queue.append(neighbor)

        return distance


if __name__ == "__main__":
    s = Solution()
    matrix = [
        [0, 1],
        [1, 0]
    ]
    print(s.shortestPathBinaryMatrix(matrix))  # 2
