from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        queue.append(root)
        res = []
        if not root: return res

        while len(queue):
            level = []
            level_size = len(queue)

            for _ in range(level_size):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)

            res.append(level[-1])

        return res


#      1
#     / \
#   3     2
#  / \     \
# 5   3     9


n1 = TreeNode(1)
n2 = TreeNode(3)
n3 = TreeNode(2)
n4 = TreeNode(5)
n5 = TreeNode(3)
n6 = TreeNode(9)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6

if __name__ == "__main__":
    instance = Solution()
    print(instance.rightSideView(n1))  # [1, 2, 9]
