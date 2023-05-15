from collections import Counter


class Solution:
    def firstUniqChar(self, s):
        ch_freq = Counter(s)

        for index, ch in enumerate(s):
            if ch_freq[ch] == 1:
                return index

        return -1


if __name__ == "__main__":
    instance = Solution()
    print(instance.firstUniqChar("leetcode"))  # 0
