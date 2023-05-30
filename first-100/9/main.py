class Solution:
    def isPalindrome(self, x):
        if x < 0 or x >= 10 and x % 10 == 0:
            return False

        values = []

        while x:
            values.append(x % 10)
            x = x // 10

        return values == values[::-1]


if __name__ == "__main__":
    instance = Solution()
    print(instance.isPalindrome(121))  # True
    print(instance.isPalindrome(-121))  # False
    print(instance.isPalindrome(10))  # False
