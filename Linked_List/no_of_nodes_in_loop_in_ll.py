#FIXME: the question is to return the no of nodes present in the loop of the given linked list.
#TODO: here we can just use the usual tortoise and hare method but a bit clever eh.

class Node:
    def __init__(self, data ,next_node = None):
        self.data = data
        self.next = next_node

def optimal_approach(head):
    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            temp = slow
            cnt = 1
            while temp.next is not slow:
                cnt = cnt+1
                temp = temp.next
            return cnt
    return -1


node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4
node5 = Node(5)
node4.next = node5

# Make a loop from node5 to node2
node5.next = node2

# Set the head of the linked list
head = node1

# Detect the loop in the linked list
ans = optimal_approach(head)
print("So the number nodes in the loop of the linked list is : ", ans)
if ans == -1:
    print("There was no loop.")
