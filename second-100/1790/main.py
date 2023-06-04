from collections import Counter


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2): return False
        diff_pos_count = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_pos_count += 1

        return diff_pos_count <= 2


if __name__ == "__main__":
    s = Solution()
    print(s.areAlmostEqual("bank", "kanb"))  # True
    print(s.areAlmostEqual("kelb", "kelb"))  # True
    print(s.areAlmostEqual("aa", "ac"))      # False
