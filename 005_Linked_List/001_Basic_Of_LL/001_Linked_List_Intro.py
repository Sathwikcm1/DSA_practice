class Node:
#TODO: using a class in python since 'struct' does not exist in python.
# by default, members in python classes are public.
    #TODO: this is a constructor,a method in class which is called automatically when an object is initiliased.
    def __init__(self,data1,next1 = None):
        self.data=data1
        self.next=next1
#TODO: self is a just a reference to the current object of the class.
#it can be of any name not just self.
if __name__ == "__main__":
    print("Finalyy reached Linked List penchoo..")
    arr = [2,3,4,6,6,7]
    n = len(arr)

    y = Node(arr[0])
    print(y) #NOTE: this will print the memory location address.
    print(y.data) #NOTE: this will print the data of the first element of the array which is 2.
    print(y.next)#NOTE: this will print the pointer to the next node, which is None as of now.
