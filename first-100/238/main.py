class Solution:
    def productExceptSelf(self, nums):
        num_count = len(nums)
        res = [1] * num_count
        prefixProduct = [1] * num_count
        postfixProduct = [1] * num_count

        for i in range(1, num_count):
            prevProduct = prefixProduct[i - 1]
            prevNum = nums[i - 1]
            prefixProduct[i] = prevProduct * prevNum

        for i in range(num_count - 2, -1, -1):
            prevProduct = postfixProduct[i + 1]
            prevNum = nums[i + 1]
            postfixProduct[i] = prevProduct * prevNum

        for i in range(num_count):
            res[i] = prefixProduct[i] * postfixProduct[i]

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
