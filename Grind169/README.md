# Tips and Patterns

## General Helpers
 - maxN = max(maxN, currN) is used a lot
 - dictionarys and hashmaps are your best friend
 - anything that could be done with a factor of O(logn) complexity lends itself to binary/tree indexing
## Array
 - When you find yourself iterating over an array for a query, consider if you could have optimized that access time from O(n) to O(1) by indexing a hashmap
 - two pointers are often crucial for some of these problems. Some ideas to consider are: pointers at the ends of an array; slow and fast pointers; sliding windows.
 - if two pointers do not work, might also want to consider divide and conquer

## 2D
 - num_rows == len(grid), then num_cols == len(grid[0]), and then the access item would be grid[row][col]. As long as you keep it consistent, it will work find
 - consider out of grid indices
 - one cool thing u can do is directions [[-1, 0], [1, 0], [0, -1], [0, 1]] and then access for directions via for dx, dy in directions

## Strings
 - sometimes, consider the ASCII value of the characters of your string
 - ord(char) -> int. chr(int) -> char (converting between ascii and str)
## Stacks
 - If you find that there are problems where order matters (i.e. validParenthesis), consider how a stack with a LIFO approach might help

## Linked Lists
 - dummy nodes could be an option!
 - dont be afraid to use more than one pointers to keep track of the original position of the head
 - consider base cases, and use small list examples to sanity check them
## Trees
 -  Often there may be DFS, BFS, recursion involved in these problems. When doing these problem, be extremely precise about the base case!
 - BFS are good for level order traversals => know how to implement VFS with queues
 - DFS can be implemented with recursion with base cases that terminates at the NULL
 - consider a bottom up approach, looking at the base cases (i.e, for height of a tree, look at how you are building up the height of the tree from 0)

## Recursion
 - BASE CASE IS ESSENTIAL, THEN find the recurrence relation

## DP
 - think in a top down approach. What is the LAST step before the final solution, and what is the relevant subproblem and reccurence relation related to this problem? To better articulate this, consider the sum of an array. Rather than consider a bottom up approach of starting from one index and adding onto the next, assume that you have a subproblem such that the next step would give you the solution. What would that be? That would be the sum of all numbers except the last. The reccurence relation then is sum(array, endIndex) = sum(array, endIndex-1) + array(endIndex) This pattern, we will see, is followed with memoization to remember subproblems that are already solved before, and some way of choosing the corrrect subproblems (often using a max) 
 - a common structure is: max_sum[i] = max(max_sum[i - 1], array[i])
# How to walkthrough a problem
 - first ask clarifying questions about the problem, and consider edge cases
 - walk through an approach, with overview of the algorthimic paradigm the problem inspires
 - write pseudocode and walk through test cases with them
 - write out the code, being sure to explain particular choices made along the way and the time complexity of the solution
 - walk through your code with test cases again to be sure it makes sense, and use SIMPLE test cases first because most edge cases can be found with just those