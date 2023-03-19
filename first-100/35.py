from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    position = 0

    while low <= high:
        candidate = (low + high) // 2
        if target == nums[candidate]:
            return candidate
        elif target > nums[candidate]:
            position = candidate + 1
            low = candidate + 1
        else:
            position = candidate
            high = candidate - 1

    return position


# print(searchInsert([1, 3, 5, 6], 5))  # 2
print(searchInsert([1, 3, 5, 6], 2))    # 1
print(searchInsert([1, 3, 5, 6], 7))    # 4
