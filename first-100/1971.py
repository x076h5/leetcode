from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, finish: int) -> bool:
        graph = self.build_graph(edges)
        stack = [start]
        visited = set()

        while len(stack):
            cur = stack.pop()
            if cur == finish: return True
            visited.add(cur)

            neighbors = graph[cur]
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)

        return False

    def build_graph(self, edges):
        graph = {}

        for edge in edges:
            a, b = edge
            if a not in graph: graph[a] = []
            if b not in graph: graph[b] = []
            graph[a].append(b)
            graph[b].append(a)

        return graph


if __name__ == "__main__":
    s = Solution()
    print(s.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))  # True
