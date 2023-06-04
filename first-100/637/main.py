from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_by_level = []
        if not root: return level_by_level
        queue = deque()
        queue.append(root)

        while len(queue):
            level = []
            level_size = len(queue)

            for _ in range(level_size):
                cur = queue.popleft()
                print(cur.val)
                level.append(cur.val)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)

            level_by_level.append(sum(level) / level_size)

        return level_by_level


#      3
#     / \
#   9    20
#  / \
# 15  7

a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)

a.left = b
a.right = c
b.left = d
b.right = e

if __name__ == "__main__":
    instance = Solution()
    print(instance.averageOfLevels(a))
