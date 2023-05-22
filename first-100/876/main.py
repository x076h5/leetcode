class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        slow = fast = head

        while fast and fast.next and fast.next.next:
            slow = head.next
            fast = head.next.next
            head = head.next

        return slow


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    instance = Solution()
    print(instance.middleNode(head))  # 3
