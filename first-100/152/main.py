from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        local_min = local_max = global_max = nums[0]

        for num in nums[1:]:
            local_max = max(num, num * local_min, num * local_max)
            local_min = min(num, num * local_min, num * local_max)
            global_max = max(global_max, local_max)

        return global_max


if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([2, 3, -2, 4]))  # 6
    print(s.maxProduct([-2, 0, -1]))  # 0
