from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num, freq = Counter(nums).most_common(1)[0]
        return num


if __name__ == "__main__":
    instance = Solution()
    print(instance.majorityElement([3, 2, 3]))
