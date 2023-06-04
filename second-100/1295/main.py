from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_len_count = 0

        for num in nums:
            str_len = len(str(num))
            if self.is_even(str_len):
                even_len_count += 1

        return even_len_count

    def is_even(self, n):
        return n % 2 == 0


if __name__ == "__main__":
    s = Solution()
    print(s.findNumbers([12, 345, 2, 6, 7896]))  # 2
