from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            cur_area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, cur_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area


if __name__ == "__main__":
    instance = Solution()
    print(instance.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
