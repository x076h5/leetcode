class Solution:
    def generate(self, row_num):
        res = []

        for i in range(row_num):
            row = [1] * (i + 1)
            for j in range(i + 1):
                if j != 0 and j != i:
                    row[j] = res[i - 1][j - 1] + res[i - 1][j]

            res.append(row)

        return res


if __name__ == "__main__":
    instance = Solution()
    print(instance.generate(5))
