# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None or head.next == None:
            return head
        
        # Swap first two nodes
        first = head
        second = head.next
        first.next = second.next
        second.next = first
        head = second
        
        # Swap remaining pairs
        prev = first  # This is the tail of the first swapped pair
        cur = first.next
        
        while cur != None and cur.next != None:
            nex = cur.next
            # Swap cur and nex
            cur.next = nex.next
            nex.next = cur
            prev.next = nex
            # Move to next pair
            prev = cur
            cur = cur.next
            
        return head
            
        