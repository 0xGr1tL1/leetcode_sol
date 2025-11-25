# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        cur = head
        prev = None
        tmp = head 
        length = 0
        count = 0
        
        # Calculate length
        while tmp != None:
            length += 1 
            tmp = tmp.next
        
        # Traverse to the node before the target
        while count != (length - n) and cur != None:
            prev = cur
            cur = cur.next
            count += 1
        
        # If removing the head node
        if prev == None:
            return head.next
        
        # Remove the target node
        prev.next = cur.next
            
        return head

