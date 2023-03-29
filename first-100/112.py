from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        stack, values = [[root, target]], []

        while len(stack):
            arr = stack.pop()
            cur, prev_sum = arr[0], arr[1]
            new_sum = prev_sum - cur.val
            if new_sum == 0 and not cur.right and not cur.left:
                return True
            if cur.right: stack.append([cur.right, cur.val])
            if cur.left: stack.append([cur.left, cur.val])

        return False



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
    print(instance.hasPathSum(n1, 15))  # True
