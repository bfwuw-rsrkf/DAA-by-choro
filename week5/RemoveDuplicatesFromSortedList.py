# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        pointer = head

        while head and head.next:
            print(head.val, head.next.val)
            
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        
        return pointer

# I decided to switch to Python, because I previously worked with it.
# For me, it is much more convenient to use Python when it comes to
# working with linked lists, because unlike Java, Python lacks all those
# ";" and "{}", and having to write all those symbols out every time
# just increases my chance of accidentally doing a mistake like that and
# having it be a huge headache, because I can be quite inattentive to
# those little details.

# So, how does my algorithm work? Simple. This is a linked list sorted in
# an ascending order, and we can abuse that. Because it is sorted this way,
# every next element must be bigger than the previous one, so we just have
# to compare our current element with the next one, see if they are equal,
# and if so - delete duplicates. There is a nuance about moving the actual
# "current" we are on though: if there are 3 or more duplicates going
# one right after another, then it may simply not end up comparing some of
# the values, when we move our "current" one step forward on line 16.

# For example, if we have 3 instances of number "2" occuring, we should not
# increment our variable right away, because if we do, then our current will
# move to the updated next without comparing it to the previous current, ending
# up with at least 2 identical numbers

# The time complexity here is O(n) in worst case and O(1) in best. Space is O(n)