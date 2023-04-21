from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive, cur_consecutive = 0, 0

        for num in nums:
            if num == 0: cur_consecutive = 0
            else: cur_consecutive += 1
            max_consecutive = max(max_consecutive, cur_consecutive)

        return max_consecutive


if __name__ == "__main__":
    s = Solution()
    print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # 3
