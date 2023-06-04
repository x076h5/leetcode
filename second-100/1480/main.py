# complexity: time - O(n) | space - O(1), where n - length of nums
def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]

    return nums


print(runningSum([1, 2, 3, 4]))  # [1, 3, 6, 10]
