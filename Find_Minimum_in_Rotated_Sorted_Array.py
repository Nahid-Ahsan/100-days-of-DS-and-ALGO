# Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

'''
This problem is binary search problem. find the mid point 
and check its left side sorted or right sorted. sorted 
side reassign the index position. this process iterate unless
get the target value.

'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]  # initially set result as 1st value
        left, right = 0, len(nums)-1  # left set zero index, right set last index

        while left<right:  # loop continue till right is greater than left
            if nums[left] < nums[right]: # check the left number is minimum, it true at last step of execution
                res = min(res,nums[left]) # find minimum from result and left value
                break  # no need to continue and break the loop
            mid = left+right//2 # find mid point/ index
            res = min(res, nums[mid])  # find minimum from result and mid value

            if nums[mid] >= nums[left]: # if mid value greater than left value then minimum value in right side
                left = mid+1  # mid index asigned to left index
            else:
                right = mid - 1  # mid index assigned to right index
        return res 
