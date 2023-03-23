# complexity: time - O(log n) | space - O(1), where n = num
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num

        while left + 1 < right:
            mid = (left + right) // 2
            if is_greater_or_equal(mid ** 2, num):
                right = mid
            else:
                left = mid

        return True if right ** 2 == num else False


def is_greater_or_equal(a: int, b: int) -> bool:
    return a >= b


if __name__ == "__main__":
    instance = Solution()
    print(instance.isPerfectSquare(16))  # True
    print(instance.isPerfectSquare(14))  # False
