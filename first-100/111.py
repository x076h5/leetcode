from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        depth = 0

        while len(queue):
            level_size = len(queue)
            depth += 1

            for _ in range(level_size):
                cur = queue.popleft()
                if not cur.left and not cur.right:
                    return depth
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)


#      1
#     / \
#   7     0
#  / \
# 7  -8


n1 = TreeNode(1)
n2 = TreeNode(7)
n3 = TreeNode(0)
n4 = TreeNode(7)
n5 = TreeNode(-8)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

if __name__ == "__main__":
    instance = Solution()
    print(instance.minDepth(n1))  # 2
