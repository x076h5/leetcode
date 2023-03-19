# complexity: time - O(log n) | space - O(1)
def guessNumber(n: int) -> int:
    low = 1
    high = n

    while low <= high:
        num = (low + high) // 2
        pick = guess(num)
        if pick == 0:
            return num
        elif pick == -1:
            high = num - 1
        else:
            low = num + 1


def guess(num: int) -> int:
    if num > 6:
        return -1
    elif num < 6:
        return 1
    return 0


# print(guess(7))  # -1
print(guessNumber(10))  # 6
