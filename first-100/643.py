import math


# complexity: time - O(n), where n - length of nums | space - O(1)
def findMaxAverage(nums, k):
    win_start = 0
    win_sum = 0
    max_average = float(-math.inf)

    for win_end in range(len(nums)):
        win_sum += nums[win_end]
        win_size = win_end - win_start + 1
        if win_size >= k:
            average = win_sum / k
            max_average = max(max_average, average)
            win_sum -= nums[win_start]
            win_start += 1

    return max_average


print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # 12.75
print(findMaxAverage([5], 1))  # 5.0
print(findMaxAverage([-1], 1))  # 1.0
