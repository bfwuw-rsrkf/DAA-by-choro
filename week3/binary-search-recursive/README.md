# Recursive implementation of Binary Search

## Explanation of Recursion
Practically speaking, what recursion does is replacing a while loop.
If you look at the code of fibonacci recursion and compare it to a while loop
in the Binary Search's Iterative variant we can tell that:
1) both programs run until a certain condition is met;
2) in each "iteration" we manipulate numbers which would eventually lead to the
termination.

## Recursive approach
To make the Binary Search recursive, we need to move our changing variables
into the method's input parameters, so that they could be carried to next
iterations. If you compare the chunks of code with if statements in both variants,
you can tell that what happened was that, metaphorically, the loop was "extended"
to borders of the whole method, making the method itself a loop. The only
technical issue here is that to terminate the program in a case of not finding
the target value is a little problematic, due to the fact that originally the
"-1" value was returned outside of loop and the loop could automatically end itself
when "low" turned out to be, well, higher than "high".