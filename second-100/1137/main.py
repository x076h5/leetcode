class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        seq = [0] * (n + 1)
        seq[1] = 1
        seq[2] = 1

        for i in range(3, n + 1):
            seq[i] = seq[i - 1] + seq[i - 2] + seq[i - 3]

        return seq[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.tribonacci(4))  # 4
    print(s.tribonacci(25))  # 1389537
