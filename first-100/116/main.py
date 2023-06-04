from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque()
        queue.append(root)
        if not root: return None

        while len(queue):
            level_size = len(queue)
            prev_node = None

            for _ in range(level_size):
                cur = queue.popleft()
                if prev_node:
                    prev_node.next = cur
                prev_node = cur
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)

        return root


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
    print(instance.connect(a))
