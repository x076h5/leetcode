# complexity: time - O(log n) | space - O(1)
class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n + 1

        while left + 1 < right:
            mid = (left + right) // 2
            if guess(mid) == - 1 or guess(mid) == 0:
                right = mid
            else:
                left = mid

        return right


def guess(num: int) -> int:
    if num > 6:
        return -1
    elif num < 6:
        return 1
    return 0


if __name__ == "__main__":
    instance = Solution()
    print(guess(7))  # -1
    print(instance.guessNumber(10))  # 6
