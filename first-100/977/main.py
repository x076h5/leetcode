from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        num_count = len(nums)
        left, right = 0, num_count - 1
        res = [None] * num_count

        for i in range(num_count - 1, -1, -1):
            left_num = abs(nums[left])
            right_num = abs(nums[right])

            if left_num > right_num:
                res[i] = left_num ** 2
                left += 1
            else:
                res[i] = right_num ** 2
                right -= 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.sortedSquares([-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]
