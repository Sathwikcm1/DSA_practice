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






#TODO: This is where the insertion starts from..


#TODO: Inserting a head in a DLL.
def insert_head(head,val):
    if head is None:
        return Node(val)
    new_node = Node(val,head,None)
    head.prev = new_node
    return new_node 
    


#TODO: Inserting a tail in a DLL.
def insert_tail(head,val):
    if head is None:
        return Node(val)
    curr = head
    while curr.next:
        curr=curr.next
    new_node= Node(val,None,curr)
    curr.next = new_node
    return head


#TODO: Inserting a new node using position.
def insert_at_k(head,val,k):
    new_node = Node(val)
    if head is None:
        return Node(val)
    curr = head
    cnt = 1 
    while curr and cnt < k - 1:
        curr = curr.next
        cnt += 1 
    if cnt < k - 1:
        print("The position given is not valid.")
        return head
    new_node.next = curr.next
    if curr.next:
        curr.next.prev = new_node
    curr.next = new_node
    new_node.prev=curr
    return head

arr = [1, 2, 3, 4, 4, 5, 6]
head = arr2DLL(arr)

print("Double Linked List:")
printDLL(head)


print("Adding a new head of value 420 using insert_head function.")
head = insert_head(head,420)
printDLL(head)

print("Adding a new tail of value 69 using insert_tail function.")
head = insert_tail(head,69)
printDLL(head)

print("Adding a new node at position 4 using function insert_at_k function.")
head = insert_at_k(head,123,4)
printDLL(head)
