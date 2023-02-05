# Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/description/

'''
here, I approach hashmap data structure. It can also solved by using list.
It take extra space but reduce time complexity
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = set() # define hashmap
        for num in nums:  # iterate through the nums
            if num in hashmap: # check if num in hashmap
                return True  # if in hash, then return true
            else:
                hashmap.add(num) #else add to the hashmap
        return False  # if no duplicate then return false

