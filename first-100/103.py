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
        is_reverse = False

        while len(queue):
            cur_level_nodes = len(queue)
            level = []

            for _ in range(cur_level_nodes):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)

            if is_reverse:
                level.reverse()
            is_reverse = not is_reverse
            level_by_level.append(level)

        return level_by_level


#     12
#     / \
#   7     1
#  /     / \
# 9    10   5
#     / \
#   20  17

n1 = TreeNode(12)
n2 = TreeNode(7)
n3 = TreeNode(1)
n4 = TreeNode(9)
n5 = TreeNode(10)
n6 = TreeNode(5)
n7 = TreeNode(20)
n8 = TreeNode(17)

n1.left = n2
n1.right = n3
n2.left = n4
n3.left = n5
n3.right = n6
n5.left = n7
n5.right = n8

if __name__ == "__main__":
    instance = Solution()
    print(instance.levelOrder(n1))  # [[12], [1, 7], [9, 10, 5], [17, 20]]
