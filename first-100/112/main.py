class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, target_sum):
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


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(0)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(-8)

    instance = Solution()
    print(instance.hasPathSum(root, 15))  # True
