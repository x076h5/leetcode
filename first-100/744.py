from typing import List


# complexity: time - O(log n) | space - O(1), where n - length of letters
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = -1
        right = len(letters)

        while left + 1 < right:
            mid = (left + right) // 2
            if is_greater(letters[mid], target):
                right = mid
            else:
                left = mid
        return letters[right] if right < len(letters) else letters[0]


def is_greater(a: int, b: int) -> bool:
    return a > b


if __name__ == "__main__":
    instance = Solution()
    print(instance.nextGreatestLetter(["c", "f", "j"], "c"))  # f
    print(instance.nextGreatestLetter(["x", "x", "y", "y"], "z"))  # x
