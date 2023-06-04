from typing import List


class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        left, right = -1, len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] - mid - 1 < k:
                left = mid
            else:
                right = mid
        return k + right


if __name__ == "__main__":
    instance = Solution()
    print(instance.findKthPositive([2, 3, 4, 7, 11], 5))  # 9
    print(instance.findKthPositive([1, 2, 3, 4], 2))  # 6
    # print(instance.first_position([2, 3, 4, 7, 11], 1))  # 0
    # print(instance.first_position([2, 3, 4, 7, 11], 5))  # 3
    # 1 5 6 8 9
    # c = 5
