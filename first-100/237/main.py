class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        next = node.next
        node.val = next.val
        node.next = next.next


# 4 -> 5 -> 1 -> 9
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)

if __name__ == "__main__":
    instance = Solution()
    print(instance.deleteNode(head.next))
