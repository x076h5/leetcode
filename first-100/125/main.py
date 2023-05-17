class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = "".join(ch for ch in s if ch.isalnum()).lower()

        return formatted == formatted[::-1]


if __name__ == "__main__":
    instance = Solution()
    print(instance.isPalindrome("A man, a plan, a canal: Panama"))  # True
