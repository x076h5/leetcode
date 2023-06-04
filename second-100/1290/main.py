class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head):
        num = 0
        decimal = 0

        while head:
            num = num * 10 + head.val
            head = head.next

        # 101 = 1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 4 + 0 + 1 = 5
        power = 0
        while num:
            decimal += (num % 10) * (2 ** power)

            power += 1
            num = num // 10

        return decimal


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(0)
    head.next.next = ListNode(1)

    instance = Solution()
    print(instance.getDecimalValue(head))  # 5
