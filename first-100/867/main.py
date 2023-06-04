from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row_count = len(matrix)
        col_count = len(matrix[0])
        transposed = [[None] * row_count for _ in range(col_count)]
        # print(transposed)

        for i in range(row_count):
            for j in range(col_count):
                transposed[j][i] = matrix[i][j]

        return transposed


if __name__ == "__main__":
    instance = Solution()
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix2 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    # print(instance.transpose(matrix))
    print(instance.transpose(matrix2))
