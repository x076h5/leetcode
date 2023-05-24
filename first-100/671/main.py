class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root):
        stack = [root]
        first_min, second_min = float("inf"), float("inf")

        while stack:
            cur = stack.pop()
            if cur.val > first_min:
                second_min = min(second_min, cur.val)
            first_min = min(first_min, cur.val)
            if cur.right: stack.append(cur.right)
            if cur.left: stack.append(cur.left)

        return -1 if second_min == float("inf") else second_min


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(2)

    instance = Solution()
    print(instance.findSecondMinimumValue(root))  # -1
