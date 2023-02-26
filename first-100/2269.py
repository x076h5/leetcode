# complexity: time - O(n), where n - length of nums | space - O(1)
def divisorSubstrings(num, k):
    win_start = 0
    nums = str(num)
    counter = 0

    for win_end in range(len(nums)):
        win_size = win_end - win_start + 1
        if win_size >= k:
            x = int(nums[win_start: win_end + 1])
            if is_divisor(num, x): counter += 1
            win_start += 1

    return counter


def is_divisor(x, y):
    if y == 0: return False
    return x % y == 0


print(divisorSubstrings(240, 2))  # 2
print(is_divisor(240, 40))  # True
print(is_divisor(240, 0))  # False
