# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1
        c2 = l2
        dummy = ListNode()
        res = dummy
        carry = 0
        while c1 or c2 or carry:
            v1 = c1.val if c1 else 0
            v2 = c2.val if c2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            res.next = ListNode(val)
            res = res.next
            c1 = c1.next if c1 else None
            c2 = c2.next if c2 else None
        return dummy.next


        