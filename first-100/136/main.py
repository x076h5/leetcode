from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        XOR = 0

        for x in nums:
            XOR ^= x

        return XOR


if __name__ == "__main__":
    instance = Solution()
    print(instance.singleNumber([2, 2, 1]))  # 1
