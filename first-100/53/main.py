from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max, global_max = nums[0], nums[0]

        for num in nums[1:]:
            local_max = max(num, local_max + num)
            global_max = max(global_max, local_max)

        return global_max


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
