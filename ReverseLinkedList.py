# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        new_head=None
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
           
        #new_head = prev
        return prev