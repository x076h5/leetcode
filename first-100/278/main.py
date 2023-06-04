# complexity: time - O(log n) | space - O(1)
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n

        while left + 1 < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid

        return right


def isBadVersion(n: int) -> bool:
    return n >= 4


if __name__ == "__main__":
    inst = Solution()
    print(inst.firstBadVersion(5))  # 4
