class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1, root2):
        leafs1, leafs2 = [], []

        def helper(node, leafs):
            if not node: return
            if not node.left and not node.right:
                leafs.append(node.val)
            helper(node.left, leafs)
            helper(node.right, leafs)

        helper(root1, leafs1)
        helper(root2, leafs2)

        return leafs1 == leafs2


if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)

    instance = Solution()
    print(instance.leafSimilar(root1, root2))  # True
