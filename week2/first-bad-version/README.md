# Binary Search

## 1. Problem
We are trying to find the first bad version in an update history of an application. We are
given an "API" that determines whether a version is bad or not. The goal is to find the one
that corrupts all the version after it.

## 2. Approach
The approach is the same as in the Binary Search problem, because this problem is actually
the Binary Search problem in disguise: we are going through some numbers and stopping when
the number satisfies a certain condition. In this case - we stop when the "API" returns
"false" to us.

So, we iterate through numbers that indicate the application version, starting from the latest
version to the earliest, and because of this the loop actually goes "backwards". When the "API"
tells that a version turns out to be "good" (it returns "false", but we need the "true" value
to trigger the if statement - hence, the "!" coming before "isBadVersion"), we conclude
that the version coming after it is the first bad one and return i+1.

The very last return statement is here in case the loop ends without terminating the program.
Let's review the last iteration of the loop in such a case: i=1 -> i>0 -> the content of a loop
gets executed, and an if statement checks whether the number i=1 isBadVersion. In order to not
end the program right now 1 has to turn out to be bad, and the if statement closes without
triggering it's contents. So, to still get the answer needed, I added a return statement
which gives the solution in this very case, while also ensuring that this int method would always
have something to return - this is a rule in Java that all non-void methods must return some value.

## 3. Time Complexity
The time complexity is the same as in the Binary Search problem. The only difference is that
we start "from the other end", i.e. the i variable actually goes down. Best- and worst-case
scenarios are also mirrored, but have the same values: O(n) & O(1).

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