from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < r:
            cur_sum = nums[l] + nums[r]
            if cur_sum > target:
                r -= 1
            elif cur_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]


if __name__ == "__main__":
    instance = Solution()
    print(instance.twoSum([1, 3, 4, 5, 7, 11], 9))  # [3, 4]
