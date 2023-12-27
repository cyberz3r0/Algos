'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

def majorityElement(nums):
    mem_obj = {}
    for value in nums:
        if value in mem_obj:
            mem_obj[value] += 1
        else:
            mem_obj[value] = 1
        if mem_obj[value] > int(len(nums)/2):
            return value