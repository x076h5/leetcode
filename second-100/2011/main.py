class Solution:
    def finalValueAfterOperations(self, operations):
        x = 0

        for o in operations:
            if "+" in o:
                x += 1
            else:
                x -= 1

        return x


if __name__ == "__main__":
    instance = Solution()
    print(instance.finalValueAfterOperations(["--X", "X++", "X++"]))  # 1
