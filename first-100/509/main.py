class Solution:
    def fib(self, n) -> int:
        if n == 0: return 0
        if n == 1: return 1

        sequence = [0] * n
        sequence[0] = 1
        sequence[1] = 1

        for i in range(2, n):
            sequence[i] = sequence[i - 1] + sequence[i - 2]

        return sequence[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.fib(4))  # 1, 1, 2, 3
    print(s.fib(2))  # 1
    print(s.fib(3))  # 2
