# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n == 1:
            return nums

        m = len(nums)//2
        ls = nums[:m] #leftside
        rs = nums[m:] #rightside
        ls = self.sortArray(ls)
        rs = self.sortArray(rs)

        ls_len = len(ls)
        rs_len = len(rs)
        
        l, r, = 0, 0
        sorted_arr = [0] * n
        i = 0

        while l < ls_len and r < rs_len:
            if ls[l] < rs[r]:
                sorted_arr[i] = ls[l]
                l += 1
            else: 
                sorted_arr[i] = rs[r]
                r += 1
            i += 1
        
        while l < ls_len:
            sorted_arr[i] = ls[l]
            l += 1
            i += 1
        
        while r < rs_len:
            sorted_arr[i] = rs[r]
            r += 1
            i += 1
        
        return sorted_arr
        
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        
        lst = self.sortArray(lst)
        dummy = ListNode(0)
        new_head = dummy
        for val in lst:
            new_head.next = ListNode(val)
            new_head = new_head.next

        return dummy.next

# To be honest, I didn't even bother to figure out
# how to do it without converting everything to a list
# and back to a linked one. So, I just kept the Merge Sort
# algorithm as a separate function, and in the one that
# solves the problem itself, I just first turned everything
# into a regular list, sorted it using Merge Sort, and then
# put everything back in as a new linked list.

# Time complexity is O(nlogn), because it uses Merge Sort
# as a main resource, and all the loops inside the second
# function actually don't change the time complexity, 
# because we count only the highest polynomial tier as the
# time complexity. Space is obviously O(n), because we
# create new "cells", which grow in numbers based on the
# initial linked list we are handed.