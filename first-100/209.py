import math


# complexity: time - O(n) | space - O(1), where n - length of nums
def minSubArrayLen(target, nums):
    win_start = 0
    win_sum = 0
    min_len = math.inf

    for win_end in range(len(nums)):
        win_sum += nums[win_end]
        while win_sum >= target:
            win_size = win_end - win_start + 1
            min_len = min(min_len, win_size)
            win_sum -= nums[win_start]
            win_start += 1

    if min_len == math.inf: return 0
    return min_len


print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # 2
