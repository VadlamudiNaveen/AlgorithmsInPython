'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1) Open brackets must be closed by the same type of brackets.
2) Open brackets must be closed in the correct order.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
'''
class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        # If the string length is odd then obviously the paranthesis are not balanced
        if len(s) % 2 != 0:
             return False
        else:
            # 
            for char in s:
                    if char == ')' or char == '}' or char == ']':
                               if len(res) > 0:
                                        top_val = res[-1]
                                        if top_val == '(' and char ==')':
                                                res.pop()           
                                        elif (top_val == '{' and char =='}'):
                                                res.pop()
                                        elif (top_val == '[' and char ==']'):
                                                res.pop()
                                        else:
                                                return False
                               
                               else:
                                        return False
                    else:
                                res.append(char) 
            if len(res) == 0:
                return True

            return False
            