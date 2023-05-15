from collections import defaultdict

# complexity: time - O(n * mlogm) | space - O(n * m),
# where n - length of strs, m - length of str
class Solution:
    def groupAnagrams(self, strs):
        anagram_groups = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            anagram_groups[sorted_s].append(s)

        return anagram_groups.values()


if __name__ == "__main__":
    instance = Solution()
    print(instance.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [["bat"], ["nat","tan"], ["ate","eat","tea"]]
