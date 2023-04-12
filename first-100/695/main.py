from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_count, col_count = len(grid), len(grid[0])
        max_area = 0

        for row in range(row_count):
            for col in range(col_count):
                if self.is_land(grid, row, col):
                    max_area = max(max_area, self.island_area(grid, row, col))

        return max_area

    def is_land(self, grid, row, col):
        return grid[row][col] == 1

    def coordinates_in_bounds(self, grid, row, col):
        row_in_bounds = 0 <= row < len(grid)
        col_in_bounds = 0 <= col < len(grid[0])

        return row_in_bounds and col_in_bounds

    def island_area(self, grid, row, col, cells=0):
        grid[row][col] = 2
        cells += 1

        directions = [
            [row + 1, col],
            [row - 1, col],
            [row, col + 1],
            [row, col - 1]
        ]

        for direction in directions:
            if self.coordinates_in_bounds(grid, *direction) and self.is_land(grid, *direction):
                cells += self.island_area(grid, *direction)

        return cells


if __name__ == "__main__":
    s = Solution()
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ]
    print(s.maxAreaOfIsland(grid))  # 6
