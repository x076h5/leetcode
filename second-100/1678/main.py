class Solution:
    def interpret(self, command):
        res = ""

        for i in range(len(command)):
            if command[i] == "G":
                res += "G"
            if command[i] == "(":
                if i + 1 < len(command) and command[i + 1] == ")":
                    res += "o"
                else:
                    res += "al"

        return res


if __name__ == "__main__":
    instance = Solution()
    print(instance.interpret("G()(al)"))  # "Goal"
    print(instance.interpret("G()()()()(al)"))  # Goooal
