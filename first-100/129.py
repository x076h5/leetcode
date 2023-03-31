from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return False
        stack = [[root, 0]]
        res = 0

        while len(stack):
            cur, prev_sum = stack.pop()
            new_num = prev_sum * 10 + cur.val
            if not cur.left and not cur.right:
                res += new_num
            if cur.right: stack.append([cur.right, new_num])
            if cur.left: stack.append([cur.left, new_num])

        return res


#      4
#     / \
#   9     0
#  / \
# 5   1


root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)

if __name__ == "__main__":
    instance = Solution()
    print(instance.sumNumbers(root))
