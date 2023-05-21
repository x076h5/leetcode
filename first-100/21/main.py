class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def mergeTwoLists(self, ll1, ll2):
        dummy_node = ListNode(-1)
        prev = dummy_node

        while ll1 and ll2:
            if ll1.val < ll2.val:
                prev.next = ll1
                ll1 = ll1.next
            else:
                prev.next = ll2
                ll2 = ll2.next
            prev = prev.next

        if ll1:
            prev.next = ll1

        if ll2:
            prev.next = ll2

        return dummy_node.next


if __name__ == "__main__":
    ll1 = ListNode(5)
    ll1.next = ListNode(7)
    ll1.next.next = ListNode(10)
    ll1.next.next.next = ListNode(12)
    ll1.next.next.next.next = ListNode(20)
    ll1.next.next.next.next.next = ListNode(28)

    ll2 = ListNode(6)
    ll2.next = ListNode(8)
    ll2.next.next = ListNode(9)
    ll2.next.next.next = ListNode(25)

    instance = Solution()
    result = instance.mergeTwoLists(ll1, ll2)
    print(result)  # 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28
