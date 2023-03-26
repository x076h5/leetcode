from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        max_salary = float("-inf")
        min_salary = float("inf")
        for x in salary:
            max_salary = max(max_salary, x)
            min_salary = min(min_salary, x)

        sum = 0
        count = 0
        for x in salary:
            if min_salary < x < max_salary:
                count += 1
                sum += x

        return sum / count


if __name__ == "__main__":
    instance = Solution()
    print(instance.average([4000, 3000, 1000, 2000]))  # 2500
