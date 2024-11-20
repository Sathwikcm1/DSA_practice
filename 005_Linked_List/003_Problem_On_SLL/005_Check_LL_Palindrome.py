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











def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

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

if __name__ == "__main__":
    main()

