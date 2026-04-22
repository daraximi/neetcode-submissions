"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyTable = {None: None}
        curr = head

        # Create copies of nodes and place in hashmap
        while curr:
            copy = Node(curr.val)
            copyTable[curr] = copy
            curr = curr.next
        # Assign the right pointers for next and random for the deep copies
        curr = head
        while curr:
            copy = copyTable[curr]
            copy.next = copyTable[curr.next]
            copy.random = copyTable[curr.random]
            curr = curr.next
        return copyTable[head]
        