#FIXME: : this is like adding the values from both the lists but in ascending order.
#example; list1 = [1,2,4], list2 = [1,3,4],,, Output: [1,1,2,3,4,4]
class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

#TODO: Solution story: so we get passes the heads of two linked lists, so we traverse both of them while
#while checking whose node's value is less, and putting it in the new list which is returned at the end.

def Merge(l1,l2):
    if not l1 and not l2:
        return None
    if not l1:
        return l2
    if not l2:
        return l1 
    
    dummy = Node(0)
    x = dummy
    while l1 and l2:
        if l1.val < l2.val:
            x.next=l1
            l1=l1.next
        else:
            x.next=l2
            l2 = l2.next
        x=x.next
            #NOTE: for my dumbass who thought it should be while loop instead of just if, they are linked nodes. if you put one link the other one is also right next to it, it's not an array.
    if l1:
        x.next=l1 
    if l2:
        x.next=l2 
    return dummy.next


# Helper function to create a linked list from a Python list
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    print(" -> ".join(map(str, result)))

# Main function to test the mergeTwoLists function
def main():
    # Create two linked lists
    l1 = create_linked_list([1, 2, 4])
    l2 = create_linked_list([1, 3, 4, 7, 8])

    # Merge the lists
    merged_list = Merge(l1, l2)  # Save the result of the merge operation

    # Print the merged list
    print("Merged Linked List:")
    print_linked_list(merged_list)  # Pass the merged list to print function

# Run the main function
if __name__ == "__main__":
    main()

