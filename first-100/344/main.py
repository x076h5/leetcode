from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1

        while l < r:
            self.swap(s, l, r)
            l += 1
            r -= 1

    def swap(self, arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp


if __name__ == "__main__":
    instance = Solution()
    # print(s.swap([4, 5], 0, 1))
    s = ["h", "e", "l", "l", "o"]
    print(instance.reverseString(s))
    print(s)
