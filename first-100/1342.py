class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0

        while num > 0:
            if is_even(num):
                num /= 2
            else:
                num -= 1
            step += 1

        return step


def is_even(n: int) -> bool:
    return n % 2 == 0


if __name__ == "__main__":
    instance = Solution()
    print(instance.numberOfSteps(14))  # 6
    print(instance.numberOfSteps(123))  # 12
