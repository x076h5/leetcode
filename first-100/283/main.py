from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0

        for i in range(len(nums)):
            cur = nums[i]
            if cur != 0:
                self.swap(nums, i, j)
                j += 1

        return nums

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    instance = Solution()
    print(instance.moveZeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
