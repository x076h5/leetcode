from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_frequency = Counter(stones)

        counter = 0
        for j in jewels:
            counter += stones_frequency[j]
        return counter


if __name__ == "__main__":
    instance = Solution()
    print(instance.numJewelsInStones("aA", "aAAbbbb"))  # 3
