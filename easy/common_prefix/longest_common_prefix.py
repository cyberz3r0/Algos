'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

def longestCommonPrefix(self, strs):
    prefix = ""
    if strs == []:
        return prefix
    if len(strs) == 1:
        return strs[0]
    for index in range(len(strs[0])):
        prefix = strs[0][0:index+1]
        for i in range(1,len(strs)):
            if not strs[i].startswith(prefix):
                return prefix[0:index]
    return prefix