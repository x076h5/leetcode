from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        queue = deque()
        inverted_root = TreeNode(root.val)
        queue.append([root, inverted_root])

        while len(queue):
            level_size = len(queue)

            for _ in range(level_size):
                cur, inverted_cur = queue.popleft()

                if cur.left:
                    inverted_cur.right = TreeNode(cur.left.val)
                    queue.append([cur.left, inverted_cur.right])
                if cur.right:
                    inverted_cur.left = TreeNode(cur.right.val)
                    queue.append([cur.right, inverted_cur.left])

        return inverted_root


# [4, 2, 7, 1, 3, 6, 9]
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

if __name__ == "__main__":
    instance = Solution()
    print(instance.invertTree(root))
    print(instance.invertTree({}))
