class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        seq = [0] * n
        seq[0] = 1
        seq[1] = 2

        for i in range(2, n):
            seq[i] = seq[i - 1] + seq[i - 2]

        return seq[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(4))  # 5
