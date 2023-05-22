class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root):
        res = []

        def traversal(root, res):
            if not root: return

            traversal(root.left, res)
            traversal(root.right, res)
            res.append(root.val)

        traversal(root, res)

        return res


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(10)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(2)

    instance = Solution()
    print(instance.postorderTraversal(root))
