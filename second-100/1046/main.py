from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sorted_stones = sorted(stones)

        while len(sorted_stones) > 1:
            x = sorted_stones.pop()
            y = sorted_stones.pop()
            if x != y:
                diff = abs(x - y)
                sorted_stones.append(diff)
            sorted_stones = sorted(sorted_stones)

        if len(sorted_stones) == 0:
            return 0

        return sorted_stones[0]


if __name__ == "__main__":
    instance = Solution()
    print(instance.lastStoneWeight([2, 7, 4, 1, 8, 1]))
