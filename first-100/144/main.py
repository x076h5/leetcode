class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# iterative
class Solution:
    def preorderTraversal(self, root):
        stack, res = [root], []
        if not root: return res

        while len(stack):
            cur = stack.pop()
            res.append(cur.val)
            if cur.right: stack.append(cur.right)
            if cur.left: stack.append(cur.left)

        return res


# recursive
# class Solution:
#     def preorderTraversal(self, node):
#         res = []
#
#         def traversal(node, res):
#             if not node: return
#
#             res.append(node.val)
#             traversal(node.left, res)
#             traversal(node.right, res)
#
#         traversal(node, res)
#
#         return res


#      a
#     / \
#   b     c
#  / \   / \
# d   e f   g

a = TreeNode("a")
b = TreeNode("b")
c = TreeNode("c")
d = TreeNode("d")
e = TreeNode("e")
f = TreeNode("f")
g = TreeNode("g")

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

if __name__ == "__main__":
    instance = Solution()
    print(instance.preorderTraversal(a))  # ['a', 'b', 'd', 'e', 'c', 'f', 'g']
