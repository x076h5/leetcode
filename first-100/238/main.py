from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_count = len(nums)
        result = [1] * num_count
        left_product = [1] * num_count
        right_product = [1] * num_count

        for i in range(1, num_count):
            left_product[i] = left_product[i - 1] * nums[i - 1]

        for i in range(num_count - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]

        for i in range(num_count):
            result[i] = right_product[i] * left_product[i]

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
