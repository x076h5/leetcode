from typing import List

# complexity: time - O(k * n) | space - O(1), where n - length of nums
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            x = nums.pop()
            nums.insert(0, x)


if __name__ == "__main__":
    instance = Solution()
    print(instance.rotate([-1, -100, 3, 99], 2))
