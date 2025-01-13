#FIXME: In this question, we need to make a stack from the scratch which has all the normal functions like push, pop, top and one more special function called getMin(), which will get the minimuym element in the stack.
# it is dynamic even if the last element is popped the min element is updated.

class Minstack():
    def __init__(self):
        self.stack = []

    #TODO: class for minstack, which describes the structure of the stack mostly the same but a lil different.

    def push(self,x:int)->None:
        if not self.stack:
            min_value = x #NOTE: if the stack is empty the current element is the min value.
        else:
            min_value = min(self.stack[-1][1],x) #NOTE: this will check the updated value of min value, it is like a 2d array, [ele, min_value], min_value is updated for each insertion.

        self.stack.append((x,min_value)) #NOTE: as we can see here, we are updating both the item and the current min element known.

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
    #NOTE: since the min_value is already updated when each element is pushed it doesn't need to be updated here.
        return None 

    def top(self) ->int:
        if self.stack:
            return self.stack[-1][0] #NOTE: as mentioned before, it's a 2d array the first element(0th index)will contain the value and then it will have min_value(2nd index.)
        return None 

    def getMin(self)->int:
        if self.stack:
            return self.stack[-1][1]
        return None


#TODO: should have written a main function here.

min_stack = Minstack()
min_stack.push(3)
min_stack.push(5)
print(min_stack.getMin())  # Output: 3
min_stack.push(2)
print(min_stack.getMin())  # Output: 1
min_stack.pop()
print(min_stack.getMin())  # Output: 2
print(min_stack.top())      # Output: 2

