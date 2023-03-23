from typing import List


# complexity: time - O(log n) | space - O(1), where n - length of nums
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)

        while left + 1 < right:
            mid = (right + left) // 2
            if is_greater_or_equal(nums[mid], target):
                right = mid
            else:
                left = mid

        return right if right < len(nums) and nums[right] == target else -1


def is_greater_or_equal(a, b):
    return a >= b


if __name__ == "__main__":
    instance = Solution()
    print(instance.search([-1, 0, 3, 5, 9, 12], 9))  # 4
    print(instance.search([99, 99, 100, 100, 104, 105], 100))  # 2
    print(instance.search([5], 5))  # 0
    print(instance.search([1, 2, 3], 4))  # -1
