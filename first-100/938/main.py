class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, node, low, high):
        total = 0

        if not node: return total

        if low <= node.val <= high:
            total += node.val

        if node.val > low:
            total += self.rangeSumBST(node.left, low, high)

        if node.val < high:
            total += self.rangeSumBST(node.right, low, high)

        return total


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)

    instance = Solution()
    print(instance.rangeSumBST(root, 7, 15))  # 32
