class Solution:
    def isPowerOfThree(self, n):
        if n <= 0: return False

        def helper(n):
            if n == 1: return True
            if n % 3 != 0: return False

            return helper(n // 3)

        return helper(n)


if __name__ == "__main__":
    instance = Solution()
    print(instance.isPowerOfThree(27))  # True
