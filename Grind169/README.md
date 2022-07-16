# Tips and Patterns

## General Helpers
 - maxN = max(maxN, currN) is used a lot
 - dictionarys and hashmaps are your best friend
 - anything that could be done with a factor of O(logn) complexity lends itself to binary/tree indexing
 - when you come across different conditions, organize how they all fit together and what if statements are needed
 - XOR is a valuable operation to ingrain
 - it is important to start with simple cases that cover edge cases and to better conceptualize the indices you are working with
## Array
 - When you find yourself iterating over an array for a query, consider if you could have optimized that access time from O(n) to O(1) by indexing a hashmap
 - two pointers are often crucial for some of these problems. Some ideas to consider are: pointers at the ends of an array; slow and fast pointers; sliding windows.
 - if two pointers do not work, might also want to consider divide and conquer
 - sometimes its l < r, sometimes its l <= r. The point is to be deliberate about what the end condition is.


## 2D
 - num_rows == len(grid), then num_cols == len(grid[0]), and then the access item would be grid[row][col]. As long as you keep it consistent, it will work find
 - check for out of grid indices
 - one cool thing u can do is directions [[-1, 0], [1, 0], [0, -1], [0, 1]] and then access for directions via for dx, dy in directions
 - for bfs questions, it may be helpful to store a queue that begins with storing all squares that match a particular starting condition (level order traversal)
 - when it comes to matrix, don't be afraid to change the values in the matrix if you visit those squares, and see if that can help you

## Strings
 - sometimes, consider the ASCII value of the characters of your string
 - ord(char) -> int. chr(int) -> char (converting between ascii and str)
 - sometimes, consider iterating in the reverse order and see if that makes things easier
## Stacks
 - If you find that there are problems where order matters (i.e. validParenthesis), consider how a stack with a LIFO approach might help
 - sometimes, these problems come off as having to do something to the front of the array or whatever that you currently on. Just be attentive to when this may be useful

## Linked Lists
 - slow and fast pointers are common
 - dummy nodes could be an option!
 - dont be afraid to use more than one pointers to keep track of the original position of the head
 - consider base cases, and use small list examples to sanity check them
## Trees
 -  Often there may be DFS, BFS, recursion involved in these problems. When doing these problem, be extremely precise about the base case!
 - BFS are good for level order traversals => know how to implement VFS with queues
 - DFS can be implemented with recursion with base cases that terminates at the NULL
 - consider a bottom up approach, looking at the base cases (i.e, for height of a tree, look at how you are building up the height of the tree from 0)
 - key thing is to focus on a single node, and how do i solve that node

## Graphs
 - Often times, you want to store a hashmap that maps old nodes to new nodes
 - want to use graphs when there are relationship between objects
 - want to use directed graph when there is a relationship that can go both ways
 - know how to do a topological sort, and what that means. Namely, if and only if there exists a topological sorting, is there there are no directed cycles. 
 - Using defaultdict(set) is gold for graphs, as it also enables you to easily add nodes to nodes that don't yet exist because default dict will enable you to simply do new_node.add(some_node)
 - also, having a visited set of nodes during dfs is a must. Sometimes it could also be useful to have an additional DS for storing some info about each node (dict)

## Recursion
 - BASE CASE IS ESSENTIAL, THEN find the recurrence relation

 ## Backtracking
 - for backtracking, you probably only need to do the pop/append once each. One before the recursive call and one after the recursive call.
 - also, remember to make copies of stuff since you are backtracking
 - permutations or combinations, think backtracking
## DP
 - think in a top down approach. What is the LAST step before the final solution, and what is the relevant subproblem and reccurence relation related to this problem? To better articulate this, consider the sum of an array. Rather than consider a bottom up approach of starting from one index and adding onto the next, assume that you have a subproblem such that the next step would give you the solution. What would that be? That would be the sum of all numbers except the last. The reccurence relation then is sum(array, endIndex) = sum(array, endIndex-1) + array(endIndex) This pattern, we will see, is followed with memoization to remember subproblems that are already solved before, and some way of choosing the corrrect subproblems (often using a max) 
 - a common structure is: max_sum[i] = max(max_sum[i - 1], array[i])
 - common subproblems is that in order to solve something of length n, you need to solve something of length i
 - there are bottom up and top down approaches. Just do what you are comfortable with
 - I think for me, thinking about what the subproblem before the final solution, and what is the step to get to that final solution, and thinking about the minimal subproblem (sort of like base case) can really help solidify the understanding of the DP approach

 ## Bits
 - There are some operations that are a must know
 - XOR is good for checking if something is repeated an even number of times, or if it is the case that exaclty one of two things is true.
 - %2 is the same as &1, //2 is the same as >>2. <<2 is the same as *2. 
 - Just try to be creative with bit manipulation!
# How to walkthrough a problem
 - first ask clarifying questions about the problem, and consider edge cases
 - walk through an approach, with overview of the algorthimic paradigm the problem inspires
 - write pseudocode and walk through test cases with them to see if they meet edge cases
 - write out the code, being sure to explain particular choices made along the way
 - walk through your code with test cases again to be sure it makes sense, and use SIMPLE test cases first because most edge cases can be found with just those
 - discuss the time complexity of the algorthim

 UMPIRE (Understand(clarify with questions, happy case), Match(match to known pattern, known techniques), Plan(Pseudocode, think of edge cases), Implement(write code), Review(walk through the code like you were debugging), Evaluate(discuss Time/Space complexity).