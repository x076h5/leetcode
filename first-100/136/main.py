from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        XOR = nums[0]

        for x in nums[1:]:
            XOR ^= x

        return XOR


if __name__ == "__main__":
    instance = Solution()
    print(instance.singleNumber([2, 2, 1, 3, 3]))  # 1
