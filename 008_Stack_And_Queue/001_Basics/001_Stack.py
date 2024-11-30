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
        if self.top +1 >= self.size:
            print("Stack Overflow.")
            return
        self.top += 1
        self.arr[self.top]=x
#NOTE: first we increment the top pointer and then only we insert the element.

    def pop(self)->int:
        if self.top == -1:
            print("Stack Underflow.")
            return -1
        x=self.arr[self.top]
        self.top-=1 
        return x

    def Top(self)->int:
        if self.top == -1:
            print("Stack is empty")
            return -1
        x=self.arr[self.top]
        return x

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

