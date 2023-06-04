# complexity: time - O(log n) | space - O(1), where n = x
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x + 1

        while left + 1 < right:
            mid = (left + right) // 2
            if is_greater_or_equal(mid * mid, x):
                right = mid
            else:
                left = mid

        return right if right * right == x else right - 1


def is_greater_or_equal(a: int, b: int) -> bool:
    return a >= b


if __name__ == "__main__":
    inst = Solution()
    print(inst.mySqrt(16))  # 4
    print(inst.mySqrt(8))  # 2
