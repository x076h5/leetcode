from typing import List


# complexity: time - O(log n) | space - O(1), where n - length of nums
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)

        while left + 1 < right:
            mid = (left + right) // 2
            if is_greater_or_equal(nums[mid], target):
                right = mid
            else:
                left = mid

        return right


def is_greater_or_equal(a, b):
    return a >= b


if __name__ == "__main__":
    instance = Solution()
    print(instance.searchInsert([1, 3, 5, 6], 5))  # 2
    print(instance.searchInsert([1, 3, 5, 6], 2))  # 1
    print(instance.searchInsert([1, 3, 5, 6], 7))  # 4
    print(instance.searchInsert([1100, 1200, 1600, 1600, 1600, 3000, 4000], 1700))  # 5
    print(instance.searchInsert([1100, 1200, 1600, 1600, 1600, 3000, 4000], 1600))  # 2
