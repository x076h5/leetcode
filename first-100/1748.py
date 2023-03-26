from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums_freq = Counter(nums)

        sum = 0
        for x in nums:
            if nums_freq[x] == 1:
                sum += x
        return sum


if __name__ == "__main__":
    instance = Solution()
    print(instance.sumOfUnique([1, 2, 3, 2]))  # 4
