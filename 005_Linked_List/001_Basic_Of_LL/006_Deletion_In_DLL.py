
class Node:
    def __init__(self, data, next_node=None, back_node=None):
        self.data = data
        self.next = next_node
        self.back = back_node

# Function to convert an array into a doubly linked list
def convert_arr_DLL(arr):
    if not arr:  # Handle empty array case
        return None

    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        temp = Node(arr[i], None, prev)
        prev.next = temp
        prev = temp

    return head

# Function to delete the head of the doubly linked list
def delete_head(head):
    if not head:  # List is empty
        return None

    new_head = head.next  # Move head to next node
    if new_head:
        new_head.back = None  # Update back pointer of new head

    del head  # Delete old head
    return new_head  # Return new head

# Function to delete the tail of the doubly linked list
def delete_tail(head):
    if not head:  # List is empty
        return None

    if not head.next:  # Only one node exists
        del head  # Delete it
        return None  # Now list is empty

    temp = head

    # Traverse to find the last node
    while temp.next:
        temp = temp.next

    prev_node = temp.back  # Get the second last node

    # Update pointers
    prev_node.next = None  # Remove reference to last node
    del temp  # Delete last node

    return head  # Return original head

# Function to print the list from head to tail
def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Function to remove the kth node from the doubly linked list
def remove_kth_node(head, k):
    if not head:  # Handle empty list
        return None

    curr = head
    cnt = 0

    while curr:
        cnt += 1
        if cnt == k:
            break
        curr = curr.next

    prev_node = curr.back
    next_node = curr.next

    if prev_node is None and next_node is None:  # Only one node
        return None
    elif prev_node is None:  # Head node
        return delete_head(head)
    elif next_node is None:  # Tail node
        return delete_tail(head)

    prev_node.next = next_node  # Update previous node's next pointer
    if next_node:
        next_node.back = prev_node  # Update next node's back pointer

    curr.next = None
    curr.back = None
    del curr

    return head

# Function to delete a given node
def delete_given_node(curr):
    prev_node = curr.back
    next_node = curr.next

    if next_node is None:  # Last node
        prev_node.next = None
        curr.back = None
        del curr
        return

    prev_node.next = next_node
    next_node.back = prev_node
    curr.next = None
    curr.back = None
    del curr


# Testing the functions
arr = [1, 2, 3, 4, 5, 6]
head = convert_arr_DLL(arr)

print("Original List: ", end="")
print_list(head)

print("After deleting the head of the Linked List:")
head = delete_head(head)
print_list(head)

print("After deleting the tail of the Linked List:")
head = delete_tail(head)
print_list(head)

print("After removing the 3rd node in the current linked list:")
head = remove_kth_node(head, 3)
print_list(head)

print("After removing the node right after the head:")
delete_given_node(head.next)
print_list(head)
