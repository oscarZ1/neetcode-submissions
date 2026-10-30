# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head  
        next_check = head 

        while next_check: 
            curr = curr.next
            next_check = next_check.next 
            if not next_check: 
                return False
            else: 
                next_check = next_check.next 
            if curr == next_check: 
                return True 
        
        return False
