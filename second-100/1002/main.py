from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq_ch = Counter(words[0])

        for i in range(1, len(words)):
            cur = Counter(words[i])
            for key in freq_ch:
                if key in cur:
                    freq_ch[key] = min(freq_ch[key], cur[key])
                else:
                    freq_ch[key] = -1

        res = []
        for key in freq_ch:
            if freq_ch[key] != -1:
                res += [key] * freq_ch[key]

        return res


if __name__ == "__main__":
    instance = Solution()
    print(instance.commonChars(["bella", "label", "roller"]))  # ["e","l","l"]
