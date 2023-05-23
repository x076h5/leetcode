class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive
class Solution:
    def isUnivalTree(self, root):
        target = root.val

        def helper(root, target):
            if not root: return True

            if root.val != target:
                return False

            return helper(root.left, target) and helper(root.right, target)

        return helper(root, target)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.right.right = TreeNode(2)

    instance = Solution()
    print(instance.isUnivalTree(root))  # False
