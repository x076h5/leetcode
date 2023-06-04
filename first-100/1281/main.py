class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = [int(i) for i in str(n)]
        product = 1
        sum = 0

        for x in nums:
            product *= x
            sum += x

        return product - sum


if __name__ == "__main__":
    instance = Solution()
    print(instance.subtractProductAndSum(234))  # 15
    print(instance.subtractProductAndSum(4421))  # 21
