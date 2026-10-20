# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0

        if not head.next:
            return None

        temp = head

        while temp:
            temp = temp.next
            counter += 1
        
        numTraversals = counter - n
        temp = head
        prev = None
        if numTraversals == 0:
            return head.next
        for i in range(numTraversals):
            prev = temp
            temp = temp.next
        
        future = temp.next
        prev.next = future

        return head
        