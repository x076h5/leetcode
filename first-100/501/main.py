from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root):
        num_freq = Counter()
        max_freq = [0]

        def helper(node, max_freq):
            if not node: return

            num_freq[node.val] += 1
            max_freq[0] = max(max_freq[0], num_freq[node.val])
            helper(node.left, max_freq)
            helper(node.right, max_freq)

        helper(root, max_freq)

        return [k for k, v in num_freq.items() if v == max_freq[0]]


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)

    instance = Solution()
    print(instance.findMode(root))  # [2]
