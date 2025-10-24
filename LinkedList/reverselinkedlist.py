from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        curNode = head
        prev = None

        while curNode:
            nextNode = curNode.next
            curNode.next = prev
            prev = curNode
            curNode = nextNode
        
        return prev
            