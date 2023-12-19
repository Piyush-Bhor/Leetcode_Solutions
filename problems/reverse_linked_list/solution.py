# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        prev, curr = None, head
        while curr:
            next_node = curr.next # Get next node
            curr.next = prev # Point current node to previous node
            prev = curr # Update previous node to curent
            curr = next_node # Update current node to next 
        return prev
             
            
