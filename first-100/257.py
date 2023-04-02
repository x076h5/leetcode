from typing import Optional, List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return []
        stack = [[root, [str(root.val)]]]
        res = []

        while len(stack):
            cur, path = stack.pop()
            if self.is_leaf(cur): res.append(path)
            if cur.right: stack.append([cur.right, [*path, str(cur.right.val)]])
            if cur.left: stack.append([cur.left, [*path, str(cur.left.val)]])

        return ["->".join(path) for path in res]

    def is_leaf(self, node: TreeNode) -> bool:
        if not node.left and not node.right: return True
        return False


#      4
#     / \
#   9     0
#  / \
# 5   1


root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)

if __name__ == "__main__":
    instance = Solution()
    print(instance.binaryTreePaths(root))  # ["4->9->5", "4->9->1", "4->0"]
