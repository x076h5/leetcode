from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        min_prefix = word

        for i in range(1, len(strs)):
            cur_prefix = self.commom_prefix(word, strs[i])
            min_prefix = cur_prefix if len(cur_prefix) < len(min_prefix) else min_prefix

        return min_prefix

    def commom_prefix(self, word1, word2):
        min_word_len = len(word1) if len(word1) < len(word2) else len(word2)
        prefix = ""

        for i in range(min_word_len):
            if word1[i] == word2[i]:
                prefix += word1[i]
            else:
                break

        return prefix


if __name__ == "__main__":
    instance = Solution()
    print(instance.longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"
    # print(instance.commom_prefix("flower", "flow"))  # "flow"
