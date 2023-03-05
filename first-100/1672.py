# complexity: time - O(n^2) | space - O(1), where n - length of accounts
def maximumWealth(accounts):
    max_wealth = 0

    for i in range(len(accounts)):
        account = accounts[i]
        sum_wealth = 0
        for j in range(len(account)):
            wealth = account[j]
            sum_wealth += wealth
        max_wealth = max(max_wealth, sum_wealth)

    return max_wealth


print(maximumWealth([[1, 5], [7, 3], [3, 5]]))  # 10
