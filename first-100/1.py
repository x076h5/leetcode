# complexity: time - O(n) | space - O(n), where n - length of nums
def twoSum(nums, target):
    seen = {}

    for i, x in enumerate(nums):
        reminder = target - x
        if x in seen: return [seen[x], i]
        seen[reminder] = i

    return [-1, -1]


print(twoSum([2, 7, 11, 15], 9))  # [0, 1]
