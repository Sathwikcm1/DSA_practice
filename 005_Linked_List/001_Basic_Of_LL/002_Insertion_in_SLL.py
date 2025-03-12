class Node:
    def __init__(self,data1,next1=None):
        self.data = data1
        self.next = next1


#TODO: this is for converting an array into a linked list.
def arr2LL(arr):
    if not arr: #NOTE: if the array itself is empty return None.
        return None
    head = Node(arr[0]) #NOTE: make the first element of array as the head.
    temp = head
    #NOTE: make a copy of head to traverse and add the following array elements.
    for i in range(1,len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next 
    return head


#TODO: Just return a new node with next pointing to the previous head.
def insert_head(head,val):
    return Node(val,head)


#TODO: A Function to add a node to the end of the linked list.
def insert_tail(head,val):
    if head is None:
        return Node(val)
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = Node(val)
    return head


#TODO: A Function to add a node to the given position. here k is the position.
def insert_at_pos(head,val,k):
    if not head:
        if k == 1: #NOTE: we also have to check for the position.
            return Node(val)
        return head
    
    if k == 1:
        return Node(val,head)


    temp = head
    cnt = 1
    while temp:
        if cnt == k-1:
            new_node = Node(val,temp.next)
            temp.next= new_node
            break
        temp= temp.next
        cnt += 1 
    return head




#TODO: A function to insert node based on value.
#insert a node before with a specific value.
def insert_on_val(head,el,val):
    #NOTE: here val, is the value of the node we have to find to insert  a new node before the current node.
    if not head:
        return Node(val)
    
    if head.data == val:
        return Node(el,head)

    temp = head
    cnt = 1
    while temp.next is not None:
        if temp.next.data == val:
            new_node = Node(el,temp.next)
            temp.next = new_node
            break
        temp=temp.next
    return head




#TODO: thiss function prints the linked list.
def printLL(head):
    while head:
        print(head.data, end= " ")
        head = head.next
    print()

arr = [1,2,3,4,5,6,6,7]
head = arr2LL(arr)
print("Printing the original List as it is: ")
printLL(head)

print("Inserting 69 as head using insert_head function.")
head = insert_head(head,69)
printLL(head)


print("Inserting 420 to the tail using insert_tail function.")
head = insert_tail(head,420)
printLL(head)

print("Inserting 7 to the position of 2 using insert_at_pos function.")
head = insert_at_pos(head,7,2)
printLL(head)

print("Inserting 46 to the node before 4 using insert_at_val.")
head = insert_on_val(head,46,4)
printLL(head)
