from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        queue = deque()
        queue.append(root)

        while len(queue):
            cur = queue.popleft()
            lh = self.height(cur.left)
            rh = self.height(cur.right)
            if abs(lh - rh) > 1: return False
            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)

        return True

    def height(self, root):
        if not root: return 0

        return max(self.height(root.left), self.height(root.right)) + 1


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

if __name__ == "__main__":
    s = Solution()
    # print(s.height(root))  # 3
    print(s.isBalanced(root))  # True
