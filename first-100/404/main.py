class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root):
        stack, sum = [[root, False]], 0

        while stack:
            cur, is_left = stack.pop()
            if not cur.left and not cur.right and is_left:
                sum += cur.val
            if cur.right: stack.append([cur.right, False])
            if cur.left: stack.append([cur.left, True])

        return sum


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    instance = Solution()
    print(instance.sumOfLeftLeaves(root))  # 24
