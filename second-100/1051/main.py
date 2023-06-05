from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        counter = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                counter += 1

        return counter


if __name__ == "__main__":
    instance = Solution()
    print(instance.heightChecker([1, 1, 4, 2, 1, 3]))  # 3
