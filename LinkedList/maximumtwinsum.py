from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        curNode = slow
        while curNode:
            nextNode = curNode.next
            curNode.next = prev
            prev = curNode
            curNode = nextNode

        maxSum = 0
        first, second = head, prev
        while second:
            maxSum = max(maxSum, first.val + second.val)
            first = first.next
            second = second.next
        
        return maxSum
