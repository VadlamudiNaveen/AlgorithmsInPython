'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-10 ** 9 <= nums[i] <= 10 ** 9

'''

'''
1.  Here the Key idea, is to check, whether the arr is having duplicates or not.
2.  So i have used, set data structure to validate it.
3.  We can also use hashmap to check if it has duplicates or not.
'''

# O(N) Space
# O(N) Time

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(set(nums)) != len(nums) else False 
				
				
