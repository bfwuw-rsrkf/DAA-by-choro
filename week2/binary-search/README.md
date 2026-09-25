# Binary Search

## 1. Problem
So the main thing about this LeetCode problem is that you're required to find a target value
inside an array, but the catch is that you need to use the Binary Search algorithm, which
has the O(logn) time complexity. For now, I'll give the simpler (yet, a little slower) solution
for the problem, which has O(n) time complexity.

## 2. Approach
I solved the problem using the for loop. Just iterate through the array one number at a time
and compare the given value with the target value. If the target value is found, the program
returns current position. If not, -1 will be returned.

## 3. Time Complexity
The time complexity of my solution is generally O(n). If we break down the program using
units of time, we can see that in the worst-case scenario the program will iterate through
the whole array, check the for condition n+1 times, execute the if statement n times,
and finally return -1. The resulting polynomial will be: n+1+n+1 units of time. Thus, the
time complexity would be O(n). But if the target value would've been the first element
of the array, this would be the best-case scenario, in which both the for and if statements
would run once and immediately return the answer, resulting in a O(1) time complexity.

## 4. Space Complexity
Space complexity is also O(n). The required "cells" of memory rise linearly with the number
of elements inside the array.

## 5. Reflection
There is a possibility (actually, the intended way) of solving this problem with O(logn)
time complexity, which could be achieved, if I'm not mistaken, by continuously reducing
the size of an array. Because the array actually has all the given elements in an
ascending order, we could take a value in the middle of the array, compare it with the
target, and if it's smaller/bigger than the target value, we would be then considering
only the left/right part of the array. By continuing this division, we would eventually
find the target value much faster, given that we don't have to iterate through every element.
If you compare graphs of f(x)=n and f(x)=logn, you could see that the value of O(logn)
would be growing much slower, thus we can conclude that O(logn) solution of this problem
will be faster.