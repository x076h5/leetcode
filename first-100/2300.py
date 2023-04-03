from bisect import bisect_left
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        sorted_potions = sorted(potions)

        for spell in spells:
            expected = success / spell
            index = bisect_left(sorted_potions, expected)
            counter = len(sorted_potions) - index
            res.append(counter)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7))  # [4, 0, 3]
