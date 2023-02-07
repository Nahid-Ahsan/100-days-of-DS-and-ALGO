# Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/description/

'''
This problem is a dynamic problem. To solve this problem
find out the patterns on it. Here negative, zero , positive numbers 
has multiple patterns.
positive number simply iterate and find max product.
zero is reindexing the current product value
negative number needs to memorize both min and max number because of this "(-,-) = + " 

'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        result =  max(nums) # initially result set to maximum value of nums
        curMax, curMin = 1,1  # min and max value set as 1 because of it refers to neutral in product operation
        for num in nums:   #iterate over nums
            if num == 0:  # check num is zero or not
                curMax, curMin = 1,1  # if zero then set again min and max to 1
                continue  # ignore the value

            temp = num*curMax  # store current max value
            curMax = max(num*curMax, num*curMin,num) # find max from current value, current max and current min 
            curMin = min(temp, num*curMin,num) # find min from current value, current max and current min 
            result = max(result,curMax)   # find final result from result and current max 
        return result 