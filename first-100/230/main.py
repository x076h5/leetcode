import heapq


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k):
        heap = []
        heapq.heapify([])

        def helper(node):
            if not node: return
            if len(heap) < k:
                heapq.heappush(heap, -node.val)
            else:
                heapq.heappushpop(heap, -node.val)
            helper(node.left)
            helper(node.right)

        helper(root)

        for _ in range(k - 1):
            heap.pop()

        return abs(heap.pop())


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    instance = Solution()
    print(instance.kthSmallest(root, 2))  # 2
