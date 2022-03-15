'''
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.
'''
class Solution:
    from string import digits
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        # O(N) to Build the Stack by following the indexes.
        for i in range(len(s)):
            if ord(s[i]) >= 40 and ord(s[i]) <= 41:
                 if s[i] == ')':
                        if len(res) > 0:
                            if res[-1][0] == '(':
                                    res.pop()
                            else:
                                    res.append((s[i],i))
                        else:
                                    res.append((s[i],i))
                 
                 else:                    
                        res.append((s[i],i))
        # Converting the STring to List and checking it where to remove the extra parathesis.
        s = list(s)
        for val in res:
                s[val[1]] = -1
        return ''.join([char for char in s if char != -1])