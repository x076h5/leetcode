class Solution:
    def decompressRLElist(self, nums):
        freq, val = 0, 1
        res = []

        for i in range(0, len(nums), 2):
            arr = self.generate_array(nums[freq + i], nums[val + i])
            res = [*res, *arr]

        return res

    def generate_array(self, freq, x):
        return [x] * freq


if __name__ == "__main__":
    instance = Solution()
    print(instance.decompressRLElist([1, 2, 3, 4]))  # [2] + [4,4,4] is [2,4,4,4]
