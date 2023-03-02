def containsDuplicate(nums):
    return len(set(nums)) != len(nums)


print(containsDuplicate([1, 2, 3, 1]))  # True
print(containsDuplicate([1, 2, 3, 4]))  # False
