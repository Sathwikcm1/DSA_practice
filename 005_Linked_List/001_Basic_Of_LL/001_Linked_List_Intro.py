class Node:
#TODO: using a class in python since 'struct' does not exist in python.
# by default, members in python classes are public.
    #TODO: this is a constructor,a method in class which is called automatically when an object is initiliased.
    def __init__(self,data1,next1 = None):
        self.data=data1
        self.next=next1

#TODO: self is a just a reference to the current object of the class.
#it can be of any name not just self.
#the point of writing "if" is to confirm this program or script is running directly and not imported as a module and running.
if __name__ == "__main__":
    print("Finalyy reached Linked List penchoo..")
    arr = [2,3,4,6,6,7]
    n = len(arr)

    y = Node(arr[0])
    print(y) #NOTE: this will print the memory location address.
    print(y.data) #NOTE: this will print the data of the first element of the array which is 2.
    print(y.next)#note: this will print the pointer to the next node, which is none as of now.
