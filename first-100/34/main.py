from typing import List


# complexity: time - O(log n) | space - O(1), where n - length of nums
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        return [self.first_position(nums, target), self.last_position(nums, target)]

    def first_position(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)

        while left + 1 < right:
            mid = (left + right) // 2
            if is_greater_or_equal(nums[mid], target):
                right = mid
            else:
                left = mid

        return right if right < len(nums) and nums[right] == target else -1

    def last_position(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)

        while left + 1 < right:
            mid = (left + right) // 2
            if is_smaller_or_equal(nums[mid], target):
                left = mid
            else:
                right = mid

        return left if left < len(nums) and nums[left] == target else -1


def is_greater_or_equal(a: int, b: int) -> bool:
    return a >= b


def is_smaller_or_equal(a: int, b: int) -> bool:
    return a <= b


if __name__ == "__main__":
    instance = Solution()
    print(instance.searchRange([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
    print(instance.last_position([5, 7, 7, 8, 8, 10], 8))  # 4
    print(instance.searchRange([], 0))  # [-1, -1]
    print(instance.searchRange([5, 7, 7, 8, 8, 10], 6))  # [-1, -1]
