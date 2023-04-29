from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # iterative
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root: return 0
    #     height = 1
    #     stack = [[root, height]]
    #     max_height = 1
    #
    #     while len(stack):
    #         cur, height = stack.pop()
    #         if not cur.left or not cur.right:
    #             max_height = max(max_height, height)
    #         if cur.right: stack.append([cur.right, height + 1])
    #         if cur.left: stack.append([cur.left, height + 1])
    #
    #     return max_height

    # recursive
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

if __name__ == "__main__":
    s = Solution()
    print(s.maxDepth(root))  # 3
