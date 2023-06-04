from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        self.transpose(matrix)

    def transpose(self, matrix: List[List[int]]) -> None:
        row_count = len(matrix)
        col_count = len(matrix[0])

        for i in range(row_count):
            for j in range(i, col_count):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    instance = Solution()
    instance.rotate(matrix)
    print(matrix)
