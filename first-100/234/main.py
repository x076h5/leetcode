class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def isPalindrome(self, head):
        values = []

        while head:
            values.append(head.val)
            head = head.next

        return values == values[::-1]


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)

    instance = Solution()
    print(instance.isPalindrome(head))  # True
