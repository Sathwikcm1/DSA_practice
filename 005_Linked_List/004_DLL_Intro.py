#FIXME: DLL is also a type of linked list, where in a node it contains two reference instead of just one.
# so one can traverse from back to front and vice versa.
class Node:
    def __init__(self,data1,next=None,prev=None):
        self.data = data1
        self.next = next
        self.prev = prev

def arr2DLL(arr):
    if not arr:
        return None
    head = Node(arr[0])
    prev_node = head #NOTE: pointer to track the previous node.
    for i in range(1,len(arr)):
        temp = Node(arr[i],None,prev_node)
        prev_node.next = temp 
        prev_node = temp
    return head


def printDLL(head):
    temp = head
    while temp:
        print(temp.data,end=" ")
        temp=temp.next
    print()
    
arr = [1, 2, 3, 4, 4, 5, 6]
head = arr2DLL(arr)

print("Double Linked List:")
printDLL(head)
