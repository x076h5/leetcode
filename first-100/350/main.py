from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        freq_table = Counter(nums2)

        for num in nums1:
            if num in freq_table and freq_table[num] != 0:
                res.append(num)
                freq_table[num] -= 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.intersect([1, 2, 2, 1], [2, 2]))  # [2, 2]
