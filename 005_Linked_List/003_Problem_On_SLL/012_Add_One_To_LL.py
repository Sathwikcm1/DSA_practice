#FIXME: so we have to add 1, to the number formed by the linked list.
# example, 1->2->3 : number is 123+1 , return 124.
class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

#TODO: brute force approach

def brute_approach(head):
    num = 0
    curr=head
    while curr:
        num = num*10 + curr.val
        curr=curr.next
    num+=1 

    dummy_head=Node(-1)
    curr=dummy_head

    for digit in str(num):
        curr.next=Node(int(digit))
        curr=curr.next
    return dummy_head.next

















def create_linked_list(arr):
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Utility function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
arr = [4, 5, 6]
head = create_linked_list(arr)
print("Original List:")
print_linked_list(head)

result_head = brute_approach(head)
print("Modified List:")
print_linked_list(result_head)
