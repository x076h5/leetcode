class Solution:
    def uniquePaths(self, rows: int, cols: int) -> int:
        matrix = [[1] * cols for row in range(rows)]

        for i in range(1, rows):
            for j in range(1, cols):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

        print(matrix)

        return matrix[-1][-1]


if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3, 7))
