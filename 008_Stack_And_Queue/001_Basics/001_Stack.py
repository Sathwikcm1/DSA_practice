#TODO: Stack is a data structure which holds a certain type of data(int,double,float,string) 
#NOTE: It follows LIFO principle. Last in First Out.
# which means whichever element goes in the last will be popped first.
# Declare an array of particular size
# define a top variable, initialize it as -1.
# write functions for pop and push and size and top.

class Stack:
    def __init__(self):
        self.top=-1
        self.size=1000
        self.arr=[0] * self.size

    def push(self,x:int) -> None:
        #NOTE: we First check if the size of the stack is sane or not.
        #for that we check if top+1 is greater than or equal to the size of the stack , if it is stack overflow.

        if self.top +1 >= self.size:
            print("Stack Overflow.")
            return
        #NOTE: And then we increase the top index first and then insert the given item.

        self.top += 1
        self.arr[self.top]=x
#NOTE: first we increment the top pointer and then only we insert the element.

    #TODO: Pops the element top is pointing to and return the element.
    def pop(self)->int:
        #NOTE: check if the top is not -1, which means the stack is empty.
        if self.top == -1:
            print("Stack Underflow.")
            return -1
        #NOTE: we first take the element that top is poining to.
        x=self.arr[self.top]
        #NOTE: And then we decrease the top by one and return the element.
        self.top-=1 
        return x
    
    #TODO: This top function will return the top element present in the stack.

    def Top(self)->int:
        #TODO: check if the stack is empty or not.
        if self.top == -1:
            print("Stack is empty")
            return -1
        #TODO: Otherwise return the element top is pointing to.
        x=self.arr[self.top]
        return x

    #TODO: This function will return the current size of the stack.
    def size_s(self):
        return self.top + 1


if __name__ =="__main__":
    s = Stack()
    s.push(3)
    s.push(6)
    s.push(9)
    s.push(4)
    print("The top of the stack before poping elements : ", s.Top())
    print("The size of the stack before deleting elements: ", s.size_s())
    print("The element poped is : ",s.pop())
    print("The size of the stack after deleting an element.",s.size_s())

#NOTE: A Stack is a linear Data structure that stores elements in a specific order.
#It follows the LIFO principle.
#Basic operations: push,pop,top/peek, size, isEmpty.
#Only top most element is accessible.
#dynamic in nature it grows or shrinks based on the operations.
# Internally stacks uses either arrays(static size) or linked lists(dynamic size.)
# Evaluating postfix (Applications)
# expression conversion
# function call management
# undo/redo functionality for this is the best data structure even tho linked list is also there.
# parenthesis matching
# memory management, DFS. 
