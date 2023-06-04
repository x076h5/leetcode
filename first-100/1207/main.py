from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_freq = Counter(arr)
        seen = set()
        print(num_freq)

        for freq in num_freq.values():
            if freq in seen:
                return False
            seen.add(freq)

        return True


if __name__ == "__main__":
    instance = Solution()
    print(instance.uniqueOccurrences([1, 2, 2, 1, 1, 3]))  # True
    print(instance.uniqueOccurrences([1, 1, 2, 2]))  # False
