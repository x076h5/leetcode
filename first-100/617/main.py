from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1: return root2
        if not root2: return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.left, root2.left)

        return root1


# [1, 3, 2, 5]
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

# [2, 1, 3, null, 4, null, 7]
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

if __name__ == "__main__":
    instance = Solution()
    print(instance.mergeTrees(root1, root2))
