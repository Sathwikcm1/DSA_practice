class Node:
    def __init__(self,data,next=None):
        self.data = data 
        self.next = next

def brute_force_approach(head):
    temp = head
    stack = []

    while temp:
        stack.append(temp.data)
        temp=temp.next


    temp = head
    while temp:
        temp.data = stack.pop()
        temp = temp.next
    return head

def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

print("The reversed linked list using brute_force_approach.")
brute_force_approach(head)
print_linked_list(head)
