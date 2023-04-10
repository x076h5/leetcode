from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        counter = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if self.explore(grid, row, col, visited) == True:
                    counter += 1

        return counter

    def explore(self, grid, row, col, visited):
        row_inbounds = 0 <= row < len(grid)
        col_inboinds = 0 <= col < len(grid[0])
        if not row_inbounds or not col_inboinds:
            return False

        if grid[row][col] == "0":
            return False

        cur_pos = (row, col)
        if cur_pos in visited: return False
        visited.add(cur_pos)

        self.explore(grid, row + 1, col, visited)
        self.explore(grid, row - 1, col, visited)
        self.explore(grid, row, col + 1, visited)
        self.explore(grid, row, col - 1, visited)

        return True


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    s = Solution()
    print(s.numIslands(grid))  # 3
