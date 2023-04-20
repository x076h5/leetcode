from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        left, right = 0, 0

        for num in nums:
            val = num + left
            val = max(val, right)

            left = right
            right = val

        return max(left, right)


if __name__ == "__main__":
    s = Solution()
    print(s.rob([1, 2, 3, 1]))  # 4
