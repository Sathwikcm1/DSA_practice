#FIXME: The question is to rotate the linked list by k places, just like in arrays.
#Input: head = [1,2,3,4,5], k = 2, Output: [4,5,1,2,3]
class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

#TODO: Story: so we first calculate the length of the linked list.
#and then we normalize k(k%=len(LL)) and then if k is 0 , we just return head.
#if not, if use them same slow and fast pointers this time also.
# we move the fast pointer by k places using a forloop.
# and then move both of them pointers slow and fast pointers at a time by one place each until fast.next is null.
# when it is done slow will be pointing to the new_tail node. so we return new_head as the slow.next and the we make the fast.next as the head.
def optimal(head,k):
    if head is None or head.next is None:
        return head
    
    curr=head
    cnt=0
    while curr:
        cnt+=1
        curr=curr.next

    #NOTE: normalizing the k.
    k%=cnt
    if k == 0:
        return head
    fast=head
    slow=head
    for _ in range(k):
        fast=fast.next
    while fast.next:
        fast=fast.next
        slow=slow.next
    #NOTE: now, slow will be pointing to the new_tail node. so we make slow.next as our new head.
    new_head = slow.next
    slow.next=None
    #NOTE: connecting the original end to the head of the original linked list.
    fast.next=head
    return new_head



def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(str(current.val))
        current = current.next
    print(" -> ".join(result))

# Main function to test the optimal rotation function
def main():
    # Create a linked list
    head = create_linked_list([1, 2, 3, 4, 5])
    
    # Rotate the list by k = 2
    print("Original List: ")
    print_linked_list(head)
    k = 2
    rotated_head = optimal(head,k)
    
    # Print the rotated linked list
    print("Rotated Linked List by ",k, " place.")
    print_linked_list(rotated_head)

# Run the main function
if __name__ == "__main__":
    main()


