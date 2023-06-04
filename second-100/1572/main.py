from typing import List


class Solution:
    def diagonalSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        row_count, col_count = len(matrix), len(matrix[0])
        total = 0

        for i in range(row_count):
            for j in range(col_count):
                if i == j:
                    total += matrix[i][j]
                if i + j == n - 1:
                    total += matrix[i][j]

        if len(matrix) % 2 == 1:
            return total - matrix[n // 2][n // 2]

        return total


if __name__ == "__main__":
    s = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(s.diagonalSum(matrix))
