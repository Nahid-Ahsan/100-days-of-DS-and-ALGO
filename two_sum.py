# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/

'''
here i approach hashmap data structure.
It reduce time complexity
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # create hashmap 
        for idx, num in enumerate(nums):  #  iterate over the list of numbers
            if (target-num) in hashmap:  # check the diffrence of target and num in hashmap
                return [idx,hashmap[target-num]]  # if difference has in hashmap then return the indexs
            else:
                hashmap[num] = idx  # else store the index as a value
        return