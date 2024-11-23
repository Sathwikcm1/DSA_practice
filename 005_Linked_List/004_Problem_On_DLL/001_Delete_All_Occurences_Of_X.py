#FIXME: delete all the nodes whose values is "x" which is given, and return the dobly linked list.

class Node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

#TODO: brute force approach:
#so my plan is to scan each node for the given value and keep on deleting the node if it matches. 
#since this is a DLL we can easily have the prev node to the current node.
def brute_force(head,x):
    curr=head
    while curr:
        if curr.data==x:
            if curr.prev:
                curr.prev.next=curr.next
            else:
                head=curr.next
                #NOTE: setting the prev pointer to the right node.
            if curr.next:
                curr.next.prev=curr.prev
        curr=curr.next
    return head





def create_dll(values):
    """Creates a doubly linked list from a list of values."""
    if not values:
        return None
    head = Node(values[0])
    curr = head
    for value in values[1:]:
        new_node = Node(value)
        curr.next = new_node
        new_node.prev = curr
        curr = new_node
    return head

def print_dll(head):
    """Prints a doubly linked list."""
    result = []
    while head:
        result.append(head.data)
        head = head.next
    print("<->".join(map(str, result)))

# Example usage
if __name__ == "__main__":
    # Input: 2<->2<->10<->8<->4<->2<->5<->2
    head = create_dll([2, 2, 10, 8, 4, 2, 5, 2])
    key = 2
    print("The original doubly linked list and the value it has to be deleted is ",key)
    print_dll(head)
    # Delete all occurrences of the key
    head = brute_force(head, key)

    # Output: 10<->8<->4<->5
    print_dll(head)

