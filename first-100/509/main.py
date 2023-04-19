class Solution:
    def fib(self, n) -> int:
        if n == 0 or n == 1: return 1

        seq = [0] * n
        seq[0] = 1
        seq[1] = 1

        for i in range(2, n):
            seq[i] = seq[i - 1] + seq[i - 2]

        return seq[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.fib(4))  # 3
    print(s.fib(2))  # 1
    print(s.fib(3))  # 2
    print(s.fib(1))  # 1
    print(s.fib(0))  # 1
