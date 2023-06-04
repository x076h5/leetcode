class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root):
        if not root: return 0
        stack, sum = [[root, 0]], 0

        while stack:
            cur, prev_num = stack.pop()
            new_num = prev_num * 10 + cur.val
            if not cur.left and not cur.right:
                sum += int(str(new_num), 2)
            if cur.right: stack.append([cur.right, new_num])
            if cur.left: stack.append([cur.left, new_num])

        return sum


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)

    instance = Solution()
    print(instance.sumRootToLeaf(root))
