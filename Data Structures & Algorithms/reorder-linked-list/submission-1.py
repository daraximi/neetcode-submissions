# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid, fast = head, head
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next

        prev = None
        curr = mid
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        mid = prev
        curr = head
        while (curr and mid.next):
            next1 = curr.next
            next2 = mid.next
            
            curr.next = mid
            mid.next = next1

            curr = next1
            mid = next2