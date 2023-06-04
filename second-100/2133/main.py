from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        row_count, col_count = len(matrix), len(matrix[0])
        is_row_contain = False

        is_row_contain = all([x for x in range(row_count)])

    def check_rows(self, matrix):
        n = len(matrix)
        nums = [i for i in range(1, n + 1)]
        num_set = set(nums)

        for i in range(n):
            if matrix[i] in num_set:
                num_set.remove(matrix[i])

        return len(num_set) == 0


if __name__ == "__main__":
    s = Solution()
    matrix = [
        [1, 2, 3],
        [3, 1, 2],
        [2, 3, 1]
    ]
    print(s.checkValid(matrix))  # True
