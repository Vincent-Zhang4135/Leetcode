# Note, the solution to this problem is built on the idea of reccurence,
# that there is some underlying recursive nature to how the solutions to this
# problem can be built up, and thus I applied the dynamic programming paradigm
# to my solution. 

# Here is my attempt at the Solution, but I realized that this DP solution
# was still missing some edge cases, so I implemented solution2:
class Solution:
    def generateParenthesis(self, n):
        sub_probs = [[] for _ in range(n)]
        if n == 0:
            return []
        sub_probs[0] = ["()"]
        for i in range(1, n):
            sols = []
            for prev_sol in sub_probs[i - 1]:
                print(prev_sol)
                sols.append("(" + prev_sol + ")")
                sols.append(prev_sol + "()")
                sols.append("()" + prev_sol)
            sols = list(set(sols))
            sub_probs[i] = sols
        return sub_probs[n - 1]
    
    def generateParenthesis2(self, n):
        # need to keep track of how many open parentheses and end 
        # parentheses there are. Also note how the the number of open 
        # parentheses left must be never more than the number of end parentheses
        ret = []
        def gen(curr, open_n, close_n):
            if open_n == 0:
                curr += (")" * close_n)
                ret.append(curr)
                return
            elif open_n < close_n:
                gen(curr + ")", open_n, close_n - 1)
            gen(curr + "(", open_n - 1, close_n)

        gen("", n, n)
        return(list(set(ret)))
    
if __name__ == '__main__':
    sol1 = Solution()
    print(sol1.generateParenthesis2(6))