class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root):
        stack, smallest_letter = [[root, ""]], chr(123) * 100

        while stack:
            cur, prev_letters = stack.pop()
            cur_letter = chr(97 + cur.val)
            new_letters = cur_letter + prev_letters
            if not cur.left and not cur.right:
                smallest_letter = min(smallest_letter, new_letters)
            if cur.right: stack.append([cur.right, new_letters])
            if cur.left: stack.append([cur.left, new_letters])

        return smallest_letter


if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)

    instance = Solution()
    print(instance.smallestFromLeaf(root))
