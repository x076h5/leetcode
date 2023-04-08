from typing import List


def dfs(graph, cur, visited):
    visited.add(cur)

    for i in range(len(graph[cur])):
        if graph[cur][i] == 1:
            if i not in visited:
                dfs(graph, i, visited)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        counter = 0
        visited = set()

        for x in range(len(isConnected)):
            if x not in visited:
                counter += 1
                dfs(isConnected, x, visited)

        return counter


if __name__ == "__main__":
    s = Solution()
    print(s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
