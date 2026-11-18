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

# The whole idea of this exact algorithm (called Merge Sort) 
# is the principle called "Divide and Conquer". You subdivide
# the bigger problem into smaller ones and solve them one by one.
# So, this algorithm is recursive. It breaks down the array
# until they reach the base case, and then "merges" them back up
# by inserting them into a new sorted list in the right order.

# The second and third while loops are needed whenever there is
# something left at the end of either array, so we don't miss it.

# The time complexity is O(nlogn) and the space is O(n).

# The "logn" part of time complexity is because we recursively break
# down the array, and it is multiplied by n, which is the number
# of times we iterate through the array on each division.