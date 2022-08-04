# 729. My Calendar I
# Medium
"""
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
 

Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
 

Constraints:

0 <= start < end <= 109
At most 1000 calls will be made to book.
"""
class MyCalendar:

    def __init__(self):
        self.slots = []
        self.flag = 0 
    def book(self, start: int, end: int) -> bool:
        if len(self.slots) == 0:  
         -       self.slots.append((start,end-1))
                return True
        else:
             for values in self.slots:
                     if ((values[0] <= start <= values[1]) or (values[0] <= end-1 <= values[1])):
                        self.flag = 1
                        print(values[0],start,end,values[1])
                        break
                     
                     elif (start <= values[0] <= end-1 and start <= values[1] <= end-1):
                        self.flag =1 
                        break
        if self.flag:
                self.flag = 0
                return False
        else:
                self.slots.append((start,end-1))
                return True
                
                
                
                
              
            
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)