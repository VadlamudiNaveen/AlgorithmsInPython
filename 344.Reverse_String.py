'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        if length % 2 != 0:
            new_length = (length // 2) + 1
            last = length
            for i in range(new_length):
                    temp = s[i]
                    last = last -1
                    s[i] = s[last]
                    s[last] = temp
                    
        else: 
            new_length = (length // 2)
            last = length
            for i in range(new_length):
                    temp = s[i]
                    last = last -1
                    s[i] = s[last]
                    s[last] = temp