class Solution:
    def xorOperation(self, n, start):
        nums = [None] * n

        for i in range(len(nums)):
            nums[i] = start + 2 * i

        result = nums[0]
        for i in range(1, len(nums)):
            result ^= nums[i]

        return result


if __name__ == "__main__":
    instance = Solution()
    print(instance.xorOperation(5, 0))  # 8
