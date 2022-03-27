'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''
## Method 1

# O(N Log N) TC
# Space O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
	        return True if sorted(s) == sorted(t) else False

## Method 2

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        r1 = {}
        for val in s:
                if val not in r1:
                       r1[val] = 1
                else: 
                       r1[val] += 1
        r2 = {}
        for val in t:
                if val not in r2:
                       r2[val] = 1
                else: 
                       r2[val] += 1
        if r1 == r2:
             return True
        return False
