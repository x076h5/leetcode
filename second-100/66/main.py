from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0

        for x in digits:
            num *= 10
            num += x

        res_num = num + 1
        res_arr = []

        while res_num:
            last_digit = res_num % 10
            res_arr.insert(0, last_digit)
            res_num = res_num // 10

        return res_arr


if __name__ == "__main__":
    instance = Solution()
    print(instance.plusOne([1, 2, 3]))  # [1, 2, 4]
    print(instance.plusOne([9]))  # [1, 0]
