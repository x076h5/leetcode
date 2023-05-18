class Solution:
    def isValid(self, brackets: str) -> bool:
        if len(brackets) % 2 == 1: return False

        pairs = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []

        for bracket in brackets:
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(pairs[bracket])
            else:
                if len(stack) != 0:
                    x = stack.pop()
                    if x != bracket:
                        return False
                else:
                    return False

        return len(stack) == 0


if __name__ == "__main__":
    instance = Solution()
    print(instance.isValid("([])"))  # True
    print(instance.isValid("){"))  # False
