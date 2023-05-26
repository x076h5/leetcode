class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, node1, node2):
        if not node1 and not node2:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False

        return self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right, node2.right)


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

if __name__ == "__main__":
    instance = Solution()
    print(instance.isSameTree(root1, root2))
