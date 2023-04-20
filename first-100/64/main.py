from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row_count, col_count = len(grid), len(grid[0])
        dp = [[0] * col_count for _ in range(row_count)]
        dp[0][0] = grid[0][0]

        for i in range(1, row_count):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for j in range(1, col_count):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, row_count):
            for j in range(1, col_count):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]


if __name__ == "__main__":
    s = Solution()
    grid1 = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(s.minPathSum(grid1))  # 7
    grid2 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(s.minPathSum(grid2))  # 12
