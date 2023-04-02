from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if self.is_good_pair(i, j, nums):
                    counter += 1

        return counter

    def is_good_pair(self, i, j, arr):
        return arr[i] == arr[j] and i < j


if __name__ == "__main__":
    instance = Solution()
    print(instance.numIdenticalPairs([1, 2, 3, 1, 1, 3]))  # 4
