from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, ll: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = ll
        prev = dummy

        while prev and prev.next and prev.next.next:
            slow = prev.next
            fast = slow.next
            prev.next = self.swap_nodes(slow, fast)  # -1->2->1->...
            prev = prev.next.next

        return dummy.next

    # 2->1->...
    def swap_nodes(self, first_node, second_node):
        temp = second_node.next  # ...
        second_node.next = first_node  # 2->1
        first_node.next = temp  # 1->...

        return second_node


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    instance = Solution()
    result = instance.swapPairs(head)
    print(result)  # 2->1->4->3
