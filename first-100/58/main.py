class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return list(map(lambda x: len(x), s.split()))[-1]


if __name__ == "__main__":
    instance = Solution()
    print(instance.lengthOfLastWord("   fly me   to   the moon  "))  # 4
