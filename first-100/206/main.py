class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:
    def reverseList(self, head):
        left, right = None, head

        while right:
            next = right.next

            right.next = left
            left = right
            right = next

        return left


if __name__ == "__main__":
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)

    instance = Solution()
    result = instance.reverseList(root)
    print(result)
