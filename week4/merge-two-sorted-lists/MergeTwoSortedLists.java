// We just iterate through both lists, check which value is smaller and append it
// to the end of our resulting list. Also, because we need to return the head of
// this list, I just straight up used a stub ListNode that would always be the
// "head" of this list, or rather just a pointer to it. That's it.

class MergeTwoSortedLists {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode pointer = new ListNode(); // pointer to the head
        ListNode res = pointer; // resulting list

        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                res.next = list1;
                list1 = list1.next;
            }
            else {
                res.next = list2;
                list2 = list2.next;
            }
            res = res.next;
        }

        if (list1 != null) { // add if anything is left
            res.next = list1;
        }
        else { // we have to add this because while loop terminates the moment
            res.next = list2; // one of the two linked lists has nothing left
        } // and so the other one might still have something, so we need to check
        return pointer.next;
    }
}

// Both the time complexity and space complexity are O(n), because the complexity
// increases linearly with the input size. The best-case scenario for time complexity
// would be if both lists are empty, in which case we have linear complexity O(1)