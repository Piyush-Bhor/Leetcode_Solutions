# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        even_head = head.next
        odd_node = head
        even_node = even_head
        
        while even_node and even_node.next:
            odd_node.next = even_node.next
            odd_node = odd_node.next 
            even_node.next = odd_node.next
            even_node = even_node.next
        
        odd_node.next = even_head
        return head