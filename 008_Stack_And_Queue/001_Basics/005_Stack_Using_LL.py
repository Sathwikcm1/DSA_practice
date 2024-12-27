#FIXME: As we know stack is a linear datastructure it can be of either static or dynamic, static stack can be acheived using the arrays.
# And the dynamic stack can be acheived by implementing stack using linked lists.

class StackNode:
    def __init__(self,data):
        self.data = data
        self.next = None
#NOTE: This is the structure for linked list node. Again this has the data and the next pointer here. 
        
class Stack: 
    #TODO: this is class for stack iself, here we use the linked list node object in order to create a stack.
    def __init__(self):
        self.top = None #NOTE: this is for the pointing to the top element in the stack.
        self.size = 0 #NOTE: this is just here to keep the size of the stack,

    #TODO: this function is for pushing the items in to the stack.
    def stack_push(self,x):
        new_node = StackNode(x) #NOTE: Initiating the object of node.
        new_node.next = self.top #NOTE: making the current item.next as top(NULL).
        self.top = new_node #NOTE: making the top as the current item.
        self.size += 1
        print("Element pushed.")


    #TODO: This function is about popping the items from the stack.
    def stack_pop(self):
        if self.top is None:
            return -1
        top_data = self.top.data
        temp = self.top 
        self.top = self.top.next 
        del temp 
        self.size -= 1
        return top_data
    
    def stack_size(self):
        return self.size 

    def stack_is_empty(self):
        return self.top is None

    def stack_peek(self):
        if self.top is None:
            return -1
        return self.top.data 
    
    def print_stack(self):
        current = self.top 
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


if __name__ == "__main__":
    s = Stack()
    s.stack_push(10)
    print("Element popped : ", s.stack_pop())
    print("Stack size: ", s.stack_size())
    print("Stack empty or not?", s.stack_is_empty())
    print("Stacks top element: ",s.stack_peek())


