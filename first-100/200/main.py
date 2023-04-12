from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if self.is_land(grid, row, col):
                    counter += 1
                    self.mark_neighbors(grid, row, col)

        return counter

    def is_land(self, grid, row, col):
        return grid[row][col] == "1"

    def coordinates_in_bounds(self, grid, row, col):
        row_in_bounds = 0 <= row < len(grid)
        col_in_bounds = 0 <= col < len(grid[0])

        return row_in_bounds and col_in_bounds

    def mark_neighbors(self, grid, row, col):
        grid[row][col] = "2"
        directions = [
            [row + 1, col],
            [row - 1, col],
            [row, col + 1],
            [row, col - 1]
        ]

        for direction in directions:
            if self.coordinates_in_bounds(grid, *direction) and self.is_land(grid, *direction):
                self.mark_neighbors(grid, *direction)

        # if self.coordinates_in_boinds(grid, row + 1, col) and self.is_land(grid, row + 1, col):
        #     self.mark_neighbors(grid, row + 1, col)
        # if self.coordinates_in_boinds(grid, row - 1, col) and self.is_land(grid, row - 1, col):
        #     self.mark_neighbors(grid, row - 1, col)
        # if self.coordinates_in_boinds(grid, row, col + 1) and self.is_land(grid, row, col + 1):
        #     self.mark_neighbors(grid, row, col + 1)
        # if self.coordinates_in_boinds(grid, row, col - 1) and self.is_land(grid, row, col - 1):
        #     self.mark_neighbors(grid, row, col - 1)


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    s = Solution()
    print(s.numIslands(grid))  # 3
