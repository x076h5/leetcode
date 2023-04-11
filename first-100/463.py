from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row_count = len(grid)
        col_count = len(grid[0])
        island_perimeter = 0

        for row in range(row_count):
            for col in range(col_count):
                if self.is_land(grid, row, col):
                    island_perimeter += self.cell_perimeter(grid, row, col)

        return island_perimeter

    def is_water(self, grid, row, col):
        return grid[row][col] == 0

    def is_land(self, grid, row, col):
        return grid[row][col] == 1

    def explore_cell_side(self, grid, row, col):
        # выходит за границы
        row_inbound = 0 <= row < len(grid)
        col_inbound = 0 <= col < len(grid[0])
        if not row_inbound or not col_inbound:
            return 1

        # вода
        if self.is_water(grid, row, col):
            return 1

        # суша
        return 0

    def cell_perimeter(self, grid, row, col):
        cell_perimeter = 0
        directions = [
            [row + 1, col],
            [row - 1, col],
            [row, col + 1],
            [row, col - 1],
        ]
        for x, y in directions:
            cell_perimeter += self.explore_cell_side(grid, x, y)

        return cell_perimeter


if __name__ == "__main__":
    s = Solution()
    grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    row, col = 0, 1
    print(s.explore_cell_side(grid, row + 1, col))  # down  - 0
    print(s.explore_cell_side(grid, row - 1, col))  # up    - 1
    print(s.explore_cell_side(grid, row, col - 1))  # left  - 1
    print(s.explore_cell_side(grid, row, col + 1))  # right - 1
    print(s.cell_perimeter(grid, row, col))  # 3
    print(s.islandPerimeter(grid))  # 16
