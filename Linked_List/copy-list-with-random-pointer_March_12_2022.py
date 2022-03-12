"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def built_new(self,root):
        new_head = Node(-10000)
        new_head_1 = new_head
        new_head_2 = new_head
        address = {}
        ind = {}
        root1 = root
        count = 0
        
        while root1:
                 
                if new_head.val is -10000:
                        new_head.val = root1.val
                        address[(new_head.val,count)] = new_head
                        if root1.random is None:
                                ind[(root1.val, count)] = -100000
                        else:
                                ind[(root1.val, count)] = root1.random.val
                else:
                        new_head.next = Node(root1.val)
                        address[(new_head.next.val, count)] = new_head.next
                        if root1.random is None:
                                ind[(root1.val, count)] = -100000
                        else:
                                ind[(root1.val, count)] = root1.random.val
                        new_head = new_head.next
                
                root1 = root1.next
                count += 1
        print(address)
        print(ind)
        count = 0
       
        while new_head_1:
                print(new_head_1.val,count)
                
                if ind[(new_head_1.val,count)] != -100000:
                        print(address[(new_head_1.val, count)])
                        new_head_1.random = address[(new_head_1.val,count)]
                else: 
                        new_head_1.random = None
                
                new_head_1 = new_head_1.next
                count += 1            
       
        return new_head_2
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return self.built_new(head)
        