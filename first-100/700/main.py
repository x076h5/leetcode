class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, node, val):
        if not node: return

        if node.val == val:
            return node

        if node.val > val:
            return self.searchBST(node.left, val)

        if node.val < val:
            return self.searchBST(node.right, val)

        return None


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)

    instance = Solution()
    result = instance.searchBST(root, 15)
    print(result)
