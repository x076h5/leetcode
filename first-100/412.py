from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range(1, n + 1):
            is_fizz = i % 3 == 0
            is_buzz = i % 5 == 0
            if is_fizz and is_buzz:
                answer.append("FizzBuzz")
            elif is_fizz:
                answer.append("Fizz")
            elif is_buzz:
                answer.append("Buzz")
            else:
                answer.append(str(i))

        return answer
