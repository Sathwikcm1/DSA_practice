#FIXME: We have to rotate the chunks of the given linked lists and each chunk contains k no of nodes. at the end if there are not enough nodes. we will let it remain as it is.
#example : Input: head = [1,2,3,4,5], k = 3, output : [3,2,1,4,5]

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=None


#TODO: hard af problem.
#Story: so we divide the given list into smaller lists of length k and reverse these smaller chunks and then link them together.

def reverseKGroup(head,k):
    #NOTE: this a helper function to reverse those smaller lists.
    def reverse_linked_list(start,end):
        prev=None
        curr=start
        while curr!=end:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        return prev
    #NOTE: dummy, is a dummy node initially pointing to the head .

    dummy = ListNode(0)
    dummy.next=head
    #NOTE: group_prev is a pointer to point at the previous group of chunk. which is also currently pointing to head.
    group_prev=dummy

    while True:
        #NOTE: kth will be pointing to current nodes.
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            #NOTE: if the kth doesn't exists it means not enough to form a chunk of k nodes.
            if not kth:
                return dummy.next
        #NOTE: so next chunk will kth next node. 
        group_next=kth.next
        #NOTE: start will be pointing to the head of small chunk and end will be pointing to the end of the small chunk.
        start=group_prev.next
        end = group_next
        #NOTE: this is where we reverse the linked list.
        reverse_group=reverse_linked_list(start,end)
        #NOTE: after reversing group_prev should be point to the new_head that is reversed_group.
        group_prev.next = reverse_group
        #NOTE: start.next should be pointing to the next chunk head.
        #NOTE start will be pointing to the end of the reversed list.
        start.next=group_next
        #NOTE: previous group should be pointing to start. 
        group_prev=start




def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Main function to test the reverseKGroup function
if __name__ == "__main__":
    # Input linked list and k
    values = [1, 2, 3, 4, 5]
    k = 2

    # Create the linked list
    head = create_linked_list(values)
    print("Original Linked List:")
    print_linked_list(head)

    # Reverse nodes in k groups
    print(f"Reversed Linked List in groups of {k}:")
    new_head = reverseKGroup(head, k)
    print_linked_list(new_head)
