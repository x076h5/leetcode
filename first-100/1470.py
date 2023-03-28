from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []

        for i in range(n):
            x = nums[i]
            y = nums[n + i]
            res.append(x)
            res.append(y)

        return res


if __name__ == "__main__":
    instance = Solution()
    print(instance.shuffle([2, 5, 1, 3, 4, 7], 3))  # [2, 3, 5, 4, 1, 7]
