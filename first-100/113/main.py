class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, target_sum):
        if not root: return []
        stack, res = [[root, target_sum, [root.val]]], []

        while len(stack):
            cur, prev_sum, path = stack.pop()
            new_sum = prev_sum - cur.val
            if new_sum == 0 and not cur.left and not cur.right:
                res.append(path)
            if cur.right:
                stack.append([cur.right, new_sum, path + [cur.right.val]])
            if cur.left:
                stack.append([cur.left, new_sum, path + [cur.left.val]])

        return res


if __name__ == "__main__":
    #      1
    #     / \
    #   7     0
    #  / \   /
    # 7  -7 14

    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(0)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(-7)
    root.right.left = TreeNode(14)

    instance = Solution()
    print(instance.pathSum(root, 15))  # 2
