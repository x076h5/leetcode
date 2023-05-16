class Solution:
    def repeatedCharacter(self, s):
        letter_freq = {}

        for letter in s:
            if letter not in letter_freq:
                letter_freq[letter] = 1
            else:
                letter_freq[letter] += 1

            if letter_freq[letter] == 2:
                return letter


if __name__ == "__main__":
    instance = Solution()
    print(instance.repeatedCharacter("abccbaacz"))  # c
