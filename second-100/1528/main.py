class Solution:
    def restoreString(self, s, indices):
        res = [None] * len(s)

        for i in range(len(s)):
            res[indices[i]] = s[i]

        return "".join(res)


if __name__ == "__main__":
    instance = Solution()
    print(instance.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
