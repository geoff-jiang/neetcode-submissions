# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = head
        total = 0
        while count:
            count = count.next
            total += 1
        
        b = total - n
        print(b)

        if b == 0: 
            return head.next

        curr = head
        prev = ListNode()
        while b > 0 and curr: 
            prev = curr
            curr = curr.next
            b -= 1

        prev.next = curr.next
        return head
        