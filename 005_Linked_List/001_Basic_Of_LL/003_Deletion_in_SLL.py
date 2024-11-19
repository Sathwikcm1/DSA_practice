class Node:
    def __init__(self,data1,next1 = None):
        self.data = data1
        self.next = next1

def arr2LL(arr):
    if not arr:
        return None
    head = Node(arr[0])
    temp = head
    for i in range(1,len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
    return head

def printLL(head):
    if not head:
        print("Empty Linked list.")
    else:
        while head:
            print(head.data,end = " ")
            head = head.next
        print()

#TODO: The real deal starts from here.


#TODO: Deleting the head of the linked list.
def delete_head(head):
    if not head or head.next is None:
        return None
    temp = head
    head = head.next
    del temp
    return head


#TODO: Deleting the tail of the linked list.
def delete_tail(head):
    if not head or head.next == Node:
        return None
    temp = head
    while temp.next.next:
        temp = temp.next
    del temp.next
    temp.next = None
    return head



#TODO: Deleting a node with value of the node.
def delete_val_node(head,val):
    if not head:
        return None
    if head.data == val:
        return delete_head(head)


    temp = head
    prev = None
    while temp:
        if temp.data == val:
            prev.next = temp.next
            del temp
            return head
        prev = temp
        temp = temp.next
    print(f"The value {val} is not present in the given linked list.")
    return head



#TODO: Deleting a node by it's position.
def delete_at_pos(head,pos):
    if head is None:
        return None
    if pos == 1:
        return del_head(head)
    
    temp = head
    prev = None
    cnt = 1 
    while temp and cnt != pos:
        prev = temp
        temp = temp.next
        cnt += 1 

    if temp:
        prev.next = temp.next 
        del temp 
    else:
        print("The position is not valid.")
    return head


arr = [69,1, 2, 3,123,4, 5, 6,420]
head = arr2LL(arr)
print("Original list:")
printLL(head)

print("Deleting the head using delete_head function.")
head = delete_head(head)
printLL(head)

print("Deleting the tail using delete_tail function.")
head = delete_tail(head)
printLL(head)

print("Deleting the 4th node using delete_at_pos function.")
head = delete_at_pos(head,2)
printLL(head)

print("Deleting a node which is of value 123 using function delete_val_node.")
head = delete_val_node(head,123)
printLL(head)
