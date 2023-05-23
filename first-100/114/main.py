class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root):
        if not root: return []
        stack, dummy = [root], TreeNode(-1)
        prev = dummy

        while stack:
            cur = stack.pop()
            prev.right = cur
            prev.left = None
            prev = prev.right
            if cur.right: stack.append(cur.right)
            if cur.left: stack.append(cur.left)

        return dummy.right


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)

    instance = Solution()
    result = instance.flatten(root)
    print(result)
