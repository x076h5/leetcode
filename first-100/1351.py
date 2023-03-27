from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        counter = 0

        for row in grid:
            for x in row:
                if x < 0:
                    counter += 1

        return counter


if __name__ == "__main__":
    instance = Solution()
    print(instance.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))  # 8
    print(instance.countNegatives([[3, 2], [1, 0]]))  # 0
