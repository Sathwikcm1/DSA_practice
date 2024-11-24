#FIXME: The question is to segrate the odd part and even part of the linked list.
#example: Original List:
#1 --> 2 --> 3 --> 4 --> null
#List after segregation (Even first, Odd next):
#2 --> 4 --> 1 --> 3 --> null
#this is based on the index of the linked list. Not the value.

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" --> ")
        curr = curr.next
    print("null")

def insert_at_last(head, value):
    new_node = Node(value)
    if not head:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head








#TODO: there is no optimal or brute force there is only one solution for this.
#STORY: so we make two seperate linked lists of even or odd values only and then combine them together.
def segregate_odd_even(head):
    if not head or not head.next:
        return head
    # odd_head = odd_tail = None
    # even_head = even_tail = None
    #
    # curr = head
    # while curr:
    #     if curr.val % 2 == 0:
    #         if even_head is None:
    #             even_head = even_tail = curr
    #         else:
    #             even_tail.next = curr
    #             even_tail = even_tail.next
    #     else:
    #         if odd_head is None:
    #             odd_head = odd_tail = curr
    #         else:
    #             odd_tail.next = curr
    #             odd_tail = odd_tail.next
    #
    #     curr = curr.next
    #
    # if even_tail:
    #     even_tail.next = odd_head
    # if odd_tail:
    #     odd_tail.next = None
    # return even_head if even_head else odd_head
    odd = head
    even = head.next
    even_head = even #TODO: this is stored because after all the odd and even joining, this is what is used to join both odd and even ones.
    #NOTE: making seperate list of odd index nodes and even index nodes.
    while even and even.next:
        odd.next=even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head
    return head



head = None
head = insert_at_last(head, 1)
head = insert_at_last(head, 2)
head = insert_at_last(head, 3)
head = insert_at_last(head, 4)

print("Original List:")
print_list(head)

# Segregate odd and even
new_head = segregate_odd_even(head)

print("\nList after segregation (Even first, Odd next):")
print_list(new_head)

