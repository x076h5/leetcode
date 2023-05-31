class Solution:
    def coinChange(self, coins, target):
        dp = [float("inf")] * (target + 1)
        dp[0] = 0

        for amount in range(1, target + 1):
            for c in coins:
                if amount - c >= 0:
                    dp[amount] = min(dp[amount], dp[amount - c] + 1)

        return dp[target] if dp[target] != float("inf") else - 1


if __name__ == "__main__":
    instance = Solution()
    print(instance.coinChange([1, 2, 5], 11))  # 3
