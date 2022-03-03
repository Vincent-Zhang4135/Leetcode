# Two sum has a rather simple O(n^2) solution:
# just loop through all the sums possible sums, and it turns
# out there will be nC_2 of these, or n(n-1)/2 of these to check
# for. However, what is more interesting is how we can solve this
# problem in O(n) time. This is done by using a hashmap to check
# calculated values in constant time

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return -1
    
    def twoSum2(self, nums, target):
        # the idea is as follows: finding if two numbers add up to a target
        # is the same as asking: if we subtract the target from my curr num
        # could i find another number that is equal to this number? This is equivalent
        # because if we do, we could subtract that from the number to get 0, implying
        # that the two numbers we found add up to the target
        
        searches = {}
        for i in range(len(nums)):
            potential = target - nums[i]
            if nums[i] in searches.keys():
                return [searches[nums[i]], i]
            searches[potential] = i
            
        return -1
        

if __name__ == '__main__':
    sol1 = Solution()
    print(sol1.twoSum2([2,7,11,15], 9))