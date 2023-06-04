from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        num_count = len(nums)

        for i in range(num_count):
            counter = 0

            for j in range(num_count):
                if j != i and nums[j] < nums[i]:
                    counter += 1

            res.append(counter)

        return res


def main():
    s = Solution()
    print(s.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))  # [4, 0, 1, 1, 3]


if __name__ == "__main__":
    main()
