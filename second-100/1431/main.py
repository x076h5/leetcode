from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        kid_count = len(candies)
        result = [False] * kid_count
        max_candie_count = max(candies)

        for i in range(kid_count):
            if candies[i] + extraCandies >= max_candie_count:
                result[i] = True

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.kidsWithCandies([2, 3, 5, 1, 3], 3))  # [True, True, True, False, True]
