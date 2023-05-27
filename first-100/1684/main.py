class Solution:
    def countConsistentStrings(self, allowed, words):
        allowed_set = set(allowed)
        counter = 0

        for word in words:
            if self.check_word(word, allowed_set):
                counter += 1

        return counter

    def check_word(self, word, alphabet):
        for letter in word:
            if letter not in alphabet:
                return False

        return True


if __name__ == "__main__":
    instance = Solution()
    print(instance.countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]))  # 2
