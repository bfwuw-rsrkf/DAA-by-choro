# Binary Search

## 1. Problem
We are trying to find the first bad version in an update history of an application. We are
given an "API" that determines whether a version is bad or not. The goal is to find the one
that corrupts all the version after it.

## 2. Approach
The approach is the same as in the Binary Search problem, because this problem is actually
the Binary Search problem in disguise: we are going through some numbers and stopping when
the number satisfies a certain condition. In this case - we stop when the "API" returns
"true" to us.

## 3. Time Complexity
The time complexity is the same as in the Binary Search problem. The only difference is that
we start "from the other end", i.e. the i variable actually goes down. Best- and worst-case
are also mirrored, but have the same values: O(n) & O(1).

## 4. Space Complexity
Space complexity is O(1), which is different from the Binary Search problem, because actually
there is no array to be iterated through - we are just inputing the numbers in the
"API" to get answers, we do not actively pull something from any data structures.

## 5. Reflection
This problem can also be solved, I believe, in the same manner as in the Binary Search problem.
The trick, again, lies in "dividing and conquering" the solution. In the previous problem we
could confidently divide the array in two, because we were given a condition that the array is
sorted in an ascending order. In this case there is another thing that allows for this to be done:
the first bad version corrupts all those that come after it - which practically serves as the
same condition, because in both cases our division and comparison are just a game of "warmer/colder". 