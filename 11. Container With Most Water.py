'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 10**4
'''

        
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_val = -float('inf') 
        i = 0
        j = len(height)-1
        length = 0
        breadth = 0
        while i < j:
            if height[i] <= height[j]:
                    length = height[i]
                    breadth = abs((i+1)-(j+1))
                    i = i + 1
            else:   
                    length = height[j]
                    breadth = abs((i+1)-(j+1))
                    j = j - 1
            max_val = max(max_val,length*breadth)
        return max_val