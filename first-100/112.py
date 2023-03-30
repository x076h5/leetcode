from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        if not root: return False
        stack = [[root, target_sum]]

        while len(stack):
            cur_node, prev_sum = stack.pop()
            new_sum = prev_sum - cur_node.val
            if new_sum == 0 and not cur_node.left and not cur_node.right:
                return True
            if cur_node.right: stack.append([cur_node.right, new_sum])
            if cur_node.left: stack.append([cur_node.left, new_sum])

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
