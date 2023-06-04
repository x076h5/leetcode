from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        level_by_level = []
        if not root: return level_by_level
        queue.append(root)

        while len(queue):
            cur_level_nodes = len(queue)
            level = []

            for _ in range(cur_level_nodes):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)

            level_by_level.append(level)

        return level_by_level


#      a
#     / \
#   b     c
#  / \   / \
# d   e f   g

a = TreeNode("a")
b = TreeNode("b")
c = TreeNode("c")
d = TreeNode("d")
e = TreeNode("e")
f = TreeNode("f")
g = TreeNode("g")

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

if __name__ == "__main__":
    instance = Solution()
    print(instance.levelOrder(a))  # [['a'], ['b', 'c'], ['d', 'e', 'f', 'g']]
