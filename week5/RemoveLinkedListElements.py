# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        pointer = ListNode(0, head)
        current = pointer

        while current:
            while current.next and current.next.val == val:
                current.next = current.next.next
            current = current.next
        
        return pointer.next

# The idea here is simply iterating through the array, while checking for any
# instances of the needed element. The inner loop is used, because there might
# be several needed elements in a row.

# There was also some trouble with the case in which the first element of the
# array was the needed one too, so I had to experiment a little, and the solution
# was simply making another layer of "pointing", if I'm not mistaken

# The time complexity is actually just O(n), despite having nested loops (the inner
# loop doesn't revisit any elements out of the bounds of those that are required
# to be deleted). And the space is O(1), because we do these changes "in-place".