#FIXME:Delete the middle node of the linked list.

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next



#TODO: this is the brute force solution.
#story: simple, find out the middle node using the same method of counting the nodes and then delete the middle node.
def brute_force(head):
    temp = head
    cnt = 0
    while temp:
        cnt+=1
        temp=temp.next
    #NOTE: the reason we didn't do cnt//2 + 1, because we gonna have to delete the middle node, we have to go one node behind middle node
    res = cnt//2
    temp = head
    while temp:
        res-=1
        if res == 0:
            mid = temp.next
            temp.next=temp.next.next
            break
        temp=temp.next
    return head
#TODO:so the time complexity is O(N) +O(N/2)

def print_linked_list(head):
    temp = head
    while temp:
        print(temp.val, end=" ")
        temp = temp.next
    print()




#TODO: optimal approach, this is using fast and slow pointers.
#story: this is using the same fast and slow pointers, same way we find out the middle node and delete it.
def optimal(head):
    if head is None or not head.next:
        return None
    slow=head
    fast=head
    #NOTE:prev : because after the while, slow pointer will be pointing to the actual middle node, so we need to get to prev node of middle in order to delete the middle node.
    prev=None
    
    while fast and fast.next:
        prev=slow #NOTE: because slow will be pointing to the middle node itself.
        slow=slow.next
        fast=fast.next.next
    
    if prev:
        prev.next=slow.next
    else:
        head=head.next
    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
# Display the original linked list
print("Original Linked List: ", end="")
print_linked_list(head)

head = brute_force(head)
print("Updated after brute force :",end=" ")
print_linked_list(head)

head = optimal(head)
print("Updated after optimal: ",end =" ")
print_linked_list(head)
