# Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/description/

'''
This problem is dynamic problem. Just simply added it's prefix value and check max sum value.
and it never be negetive.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]  # set 1st value of list as a maximum value
        curSum = 0  # initially current sum value set zero
        for num in nums: # iterate over the list
            if curSum < 0: # check the current sum is negetive or not
                curSum = 0  # if current sum negetive then it set to zero again
            curSum += num  # if not negetive, then continue added 
            maxSum = max(maxSum, curSum)  # check the maximum sum and store maximum value in maxSum

        return maxSum  # return maximum value