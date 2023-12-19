# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_ptr, fast_ptr = head, head
        prev_node = None

        if head is None or head.next is None:
            return
        
        while fast_ptr is not None and fast_ptr.next is not None:
            prev_node = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        prev_node.next = slow_ptr.next
        return head