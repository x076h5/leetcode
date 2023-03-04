import math


def search(nums, target):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = math.ceil((high + low) / 2)
        cur = nums[mid]
        if target == cur:
            return mid
        elif target > cur:
            low = mid - 1
        else:
            high = mid + 1

    return -1


print(search([-1, 0, 3, 5, 9, 12], 9))
