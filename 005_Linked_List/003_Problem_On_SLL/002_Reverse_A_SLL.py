#FIXME: The question is to return the reversed linked list for the given linked list.

class Node:
    def __init__(self,data,next=None):
        self.data = data 
        self.next = next

        #TODO: the story of this one is just we are putting all the elements of the LL to  a stack.
        #so we can pop elements from the stack one by one and put it back to the linked list.
        #"so we are traversing the LL two times." so that would take the time complexity to O(N) + O(N) = O(2N)
def brute_force_approach(head):
    temp = head
    stack = []

    while temp:
        stack.append(temp.data)
        temp=temp.next

    #NOTE: reinitialsing the temp because it will be pointing to null after the first loop.
    temp = head
    while temp:
        temp.data = stack.pop()
        temp = temp.next
    return head

#FIXME : just a print function here.
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

def optimal_approach(head):
    curr = head
    prev_node =None

    while curr:
        next_node = curr.next #NOTE: next_node will point to next node to the current node.
        curr.next = prev_node #NOTE: then we will move current nodes next as previous node.
        prev_node = curr #NOTE: then we make the previous node as the current node. 
        curr = next_node #NOTE: then we make the current node to the next node.
    return prev_node #NOTE: because the current pointer will be pointing to null.


head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

print("The reversed linked list using brute_force_approach.")
brute_force_approach(head)
print_linked_list(head)

print("The reversed linked list using optimal_approach")
head = optimal_approach(head)
print_linked_list(head)
