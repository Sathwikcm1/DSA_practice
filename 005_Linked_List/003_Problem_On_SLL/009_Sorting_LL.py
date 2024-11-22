#FIXME: Return a sorted linked list based on the value ofcourse.

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

#TODO: this is the brute force solution.
#story: put all the values into an array and then sort it and put it back in the linked list.
def brute_force(head):
    arr = []
    temp=head
    while temp:
        arr.append(temp.val)
        temp=temp.next
    
    arr.sort()
    temp= head
    for i in range(len(arr)):
        temp.val=arr[i]
        temp=temp.next

    return head












def print_linked_list(head):
    temp = head
    while temp is not None:
        # Print the data of the current node
        print(temp.data, end=" ")
        # Move to the next node
        temp = temp.next
    print()


# Linked List: 3 2 5 4 1
head = Node(3)
head.next = Node(2)
head.next.next = Node(5)
head.next.next.next = Node(4)
head.next.next.next.next = Node(1)

print("Original Linked List: ", end="")
print_linked_list(head)
print("After brute force solution to sort the list:")
head=brute_force(head)
print_linked_list(head)
