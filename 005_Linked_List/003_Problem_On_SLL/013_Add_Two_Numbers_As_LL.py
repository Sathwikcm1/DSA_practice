#FIXME: return the sum of the number formed by the values of two linked lists.
#example: num1 = 243, num2=564 and sum = 807 , return a LL with that value.

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

#TODO: brute force solution.
#story: so we represent the actual number 342 as 2->4->3, yes it is reverse, so we will take a dummy head 
# and we will have a carry for addition if there comes a carry, the loop runs as long as list or carry exists.
# we will take the values. we caculate the total.
def brute_force(l1,l2):
    dummy_head = Node(-1)
    curr=dummy_head
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total=val1 + val2 + carry
        curr.next=Node(total%10)
        carry=total//10
        curr=curr.next

        if l1:
            l1=l1.next
        if l2:
            l2=l2.next
    return dummy_head.next



def create_linked_list(values):
    """Create a linked list from a list of values."""
    dummy_head = Node(-1)
    curr = dummy_head
    for val in values:
        curr.next = Node(val)
        curr = curr.next
    return dummy_head.next

def print_linked_list(node):
    """Print a linked list as a sequence of numbers."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(" -> ".join(map(str, result)))



if __name__ == "__main__":
    l1 = create_linked_list([2, 4, 3])  # Represents 342
    l2 = create_linked_list([5, 6, 4])  # Represents 465

    result = brute_force(l1, l2)

    print("Result:")
    print_linked_list(result)  # Should output: 7 -> 0 -> 8
