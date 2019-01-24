# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2 ,c = 0):
        # This node doesn't get included in the final list.
        newHead = ListNode(0)
        curNode = newHead
        carry = 0
        
        while l1 is not None or l2 is not None:            
            total = 0
            total += carry 
            
            if l1 is not None:
                total += l1.valsa
            if l2 is not None:
                total += l2.val
            
            carry = total // 10
            total = total % 10
            
            # reuse the existing nodes instead of creating new memory.
            reUseNode = l1 if l1 is not None else l2
            
            # Add the next node to the list
            reUseNode.val = total
            curNode.next = reUseNode
            curNode = curNode.next
            
            # Move the lists forward if they aren't already finished.
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            
        # Check for remaining carry
        if carry > 0:
            curNode.next = ListNode(1)
            
        return newHead.next
