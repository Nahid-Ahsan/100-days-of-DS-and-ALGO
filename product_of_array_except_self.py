# Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/

'''
This problem solved many optimal way. I choose two pointer. 
this pointers works as prefix and postfix method.
Once calculate the product of  given list in order and then reverse order.
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]* len(nums)  # define a list of answer with value 1 in same length of nums

        prefix = 1    # define prefix
        for i in range(len(nums)):   # iterate in-order 
            answer[i] *= prefix  #  answer value multiply with prefix
            prefix *= nums[i]  # prefix increament with product of nums value

        postfix = 1  # define postfix
        for i in range(len(nums)-1,-1,-1):  # iterate through reverse order
            answer[i] *= postfix  # answer value multiply with postfix
            postfix *= nums[i]  # postfix value increament with product of reverse order nums value

        return answer 
'''
Explaination:
nums = [1,2,3,4]



'''