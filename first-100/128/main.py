class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        max_consecutive = 0

        for num in nums:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1

                max_consecutive = max(max_consecutive, length)

        return max_consecutive


if __name__ == "__main__":
    instance = Solution()
    print(instance.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4
