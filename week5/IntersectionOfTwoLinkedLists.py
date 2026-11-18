class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lista = headA
        listb = headB

        while lista != listb:
            if lista:
                lista = lista.next
            else:
                lista = headB

            if listb:
                listb = listb.next
            else:
                listb = headA
        
        return listb

listA = ListNode(4, ListNode(1, ListNode(8, ListNode(4, ListNode(5)))))              #[4,1,8,4,5,5,6,1,8,4,5]
listB = ListNode(5, ListNode(6, ListNode(1, ListNode(8, ListNode(4, ListNode(5)))))) #[5,6,1,8,4,5,4,1,8,4,5]
print(Solution.getIntersectionNode(listA, listB))

# Initially I thought about making a nested loop and iterating through each element of the second loop,
# while comparing it to an element from the first one by one, but this would be O(n^2) time complexity.
# This idea came to me, because there would be cases of linked lists having different lengths, which
# would cause a massive problem with just straight ahead parallel iterating through both of those lists.

# But, there was a sort of a hint at the end of the description of this problem:
# "Could you write a solution that runs in O(m + n) time and use only O(1) memory?"
# If I summed the arrays, I would solve the problem of having different lengths
# AND I would be able to iterate through them straight up.

# Using while loop with the "lista != listb" condition allowed me tot avoid any
# comparisons inside the loop, and all that was there to do is just keep incrementing
# our "pointers"

# Time complexity is O(n) and space is O(1)