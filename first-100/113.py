from typing import Optional, List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
        res = []
        if not root: return res
        stack = [[root, target_sum, [root.val]]]

        while len(stack):
            cur, prev_sum, path = stack.pop()
            new_sum = prev_sum - cur.val
            print(path)
            if new_sum == 0 and not cur.left and not cur.right:
                res.append(path)
            if cur.right: stack.append([cur.right, new_sum, path + [cur.right.val]])
            if cur.left: stack.append([cur.left, new_sum, path + [cur.left.val]])

        return res


#      1
#     / \
#   7     0
#  / \   /
# 7  -8 14


n1 = TreeNode(1)
n2 = TreeNode(7)
n3 = TreeNode(0)
n4 = TreeNode(7)
n5 = TreeNode(-8)
n6 = TreeNode(14)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6

if __name__ == "__main__":
    instance = Solution()
    print(instance.pathSum(n1, 15))  # 2
