# this question asks us to build up an array that has
# no duplicates. This clearly can be run in O(n) time, 
# as we can simply loop through the array once and remove duplicates
# along the way. The more interesting part of this problem is that we want 
# the solution to be stored in the first k elements of the array. My solution
# keeps track of a different index from the index that we are using to loop 
# through the array, so we know where to put "new" values in the actual array:

class Solution:
    def removeDuplicates(self, nums):
        prev = 0.1
        curr_i = 0
        for i in range(len(nums)):
            if nums[i] == prev:
                continue
            else:
                nums[curr_i] = nums[i]
                prev = nums[curr_i]
                curr_i += 1
                
        return curr_i
    
if __name__ == '__main__':
    sol1 = Solution()
    print(sol1.removeDuplicates([1, 2, 2, 2, 3, 4, 5, 6, 6, 7, 8, 8, 9]))