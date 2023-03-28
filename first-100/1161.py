from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        level_res = 0
        cur_level = 0
        max_level_sum = 0

        while len(queue):
            cur_level += 1
            level_size = len(queue)
            level_sum = 0
            for _ in range(level_size):
                cur = queue.popleft()
                level_sum += cur.val
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)

            if max_level_sum < level_sum:
                max_level_sum = level_sum
                level_res = cur_level

        return level_res


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
    print(instance.maxLevelSum(n1))
