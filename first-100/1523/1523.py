# complexity: time - O(1) | space - O(1)
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd_count = (high - low) // 2
        if is_odd(low) or is_odd(high):
            odd_count += 1
        return odd_count


def is_odd(x: int) -> bool:
    return x % 2 == 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.countOdds(3, 7))  # 3
    print(solution.countOdds(7, 10))  # 2
    print(solution.countOdds(21, 22))  # 1
    print(solution.countOdds(2, 4))  # 1
