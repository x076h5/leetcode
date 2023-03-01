class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverseList(head):
    cur = head
    prev = None

    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    return prev


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4

print(reverseList(n1))
