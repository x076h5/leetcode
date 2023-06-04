class Solution:
    def luckyNumbers(self, matrix):
        row_count, col_count = len(matrix), len(matrix[0])
        lucky_nums = []

        row_min_nums = set()
        for i in range(row_count):
            row_min_nums.add(min(matrix[i]))

        for i in range(col_count):
            col_nums = []
            for j in range(row_count):
                col_nums.append(matrix[j][i])

            col_max_num = max(col_nums)
            if col_max_num in row_min_nums:
                lucky_nums.append(col_max_num)

        return lucky_nums


if __name__ == "__main__":
    matrix = [
        [3, 7, 8],
        [9, 11, 13],
        [15, 16, 17]
    ]
    instance = Solution()
    print(instance.luckyNumbers(matrix))  # [15]
