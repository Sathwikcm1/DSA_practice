#FIXME: the question is to find out if a linked list is a palindrome or not.


class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

#TODO: Brute force approach:
#story: use a stack data structure to store the values of the LL. and them pop them and check for each value is same for original LL.
def brute_force_approach(head):
    st = []
    temp = head
    while temp:
        st.append(temp.data)
        temp=temp.next

    temp = head
    while temp:
        if temp.data != st.pop():
            return False
        temp=temp.next
    return True

#TODO: the time complexity is O(2*N).


#TODO: this works using recursion.
def reverse_linked_list(head):
    if not head or not head.next:
        return head

    new_head = reverse_linked_list(head.next)
    front = head.next
    front.next = head
    head.next = None
    return new_head


#     slow=head
#     fast=head
#     while fast and fast.next:
#         fast=fast.next.next
#         slow=slow.next
#     #NOTE: this is where we get the middle of the linked list, slow will be pointing to the middle of the linked list.
#     # so we reverse the other half from the slow.next, we reverse the linked list.
#     new_head = reverse_linked_list(slow.next)
#     first_half = head
#     second_half = new_head
#
#     while second_half:
#         if first_half.data != second_half.data:
#             reverse_linked_list(new_head)
#             return False
#         first_half=first_half.next
#         second_half=second_half.next
#     reverse_linked_list(new_head)
#     return True
#


def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()



#TODO: story: in this we use the same slow and fast pointer to find out the middle node of the linked list.
#once we do then we will reverse the second half of the linked list using middle node we just found out.
# and then we check for each value, return true or false accordingly before that we have to reverse the linked list.
# def optimal_approach(head):
#     if not head or not head.next:
#         return True #TODO: this means empty linked is a palindrome.
#
#TODO: story: we reverse the linked list from the middle, excluding the middle node.
#and then we compare the first half and the second half of the linked list if they are same values or not.
#and the second while loop will run till slow is none.
def optimal_approach(head):
    if not head or not head.next:
            return True
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    #NOTE: now slow is pointing to the middle node of the linked list.
    prev  = None #NOTE: this is used for reversing the linked list.
    while slow:
        temp = slow.next
        slow.next = prev
        prev=slow
        slow=temp
    #NOTE: left represents head of the first half of the linked list. Right represets the other half head, right next to the middle node.
    left,right=head,prev
    while right:
        if left.data != right.data:
            return False
        left=left.next
        right= right.next
    return True

def main():
    # Create a linked list with
    # values 1, 5, 2, 5, and 1 (15251, a palindrome)
    head = Node(1)
    head.next = Node(5)
    head.next.next = Node(2)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(1)

    # Print the original linked list
    print("Original Linked List: ", end="")
    print_linked_list(head)

    # Check if the linked list is a palindrome
    if brute_force_approach(head):
        print("The linked list is a palindrome.")
    else:
        print("The linked list is not a palindrome.")

    if optimal_approach(head):
        print("The linked list is a Palindrome.")
    else:
        print("The linked list is not a palindrome.")
if __name__ == "__main__":
    main()

