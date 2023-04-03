from bisect import bisect_left
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        sorted_potions = sorted(potions)

        for spell in spells:
            expected = success / spell
            # индекс первого элемента большего или равного ожидаемому
            index = bisect_left(sorted_potions, expected)
            counter = len(sorted_potions) - index
            res.append(counter)

        return res

    # class Solution:
    #     def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
    #         res = []
    #
    #         for i in range(len(spells)):
    #             counter = 0
    #
    #             for j in range(len(potions)):
    #                 is_successful_pair = spells[i] * potions[j] >= success
    #                 if is_successful_pair: counter += 1
    #
    #             res.append(counter)
    #
    #         return res


if __name__ == "__main__":
    s = Solution()
    print(s.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7))  # [4, 0, 3]
