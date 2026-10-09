// I initially thought of saving the values of this list somewhere
// and checking if the next value is present in the previous ones,
// but this one could get really complex really fast, so I needed
// a different solution. Also, it's not explicitly stated in the
// description of the problem, but I think it's implied that there
// are only unique values. Eventually I came to the idea of iterating
// twice through the list at the same time. Even if the space between
// the cycle's values is uneven, if I'm not mistaken, if it is present,
// then the second "iterator" would eventually circle back.

public class LinkedListCycle {
    public boolean hasCycle(ListNode head) {
        ListNode oneStep = head;
        ListNode twoStep = head;

        while (twoStep != null && twoStep.next != null) { // the cycle depends
            oneStep = oneStep.next; // on the twoStep "iterator". If it can't
            twoStep = twoStep.next.next; // make it's "jump", then we return
            if (oneStep == twoStep) { // false right away.
                return true;
            }
        }
        return false;
    }
}

// Both the time complexity and space complexity are O(n), because the complexity
// increases linearly with the input size. The best-case scenario for time complexity
// would be if the list is empty, in which case we have linear complexity O(1)