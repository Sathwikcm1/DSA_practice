#FIXME: try to sort a linked list which only contains the values 0,1 and 2s.
# 1->0->1->1->0->2->0->2
# counter[3,3,2] , after result will be: 0->0->0->1->1->1->2->2.

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

#TODO:brute force solution.
#story: we make a counter list, where the indexes 0, 1 and 2 acts as a counter for the numbers themselves.
#after that we put the count no of numbers into the linked list using while loop.

def brute(head):
    count = [0,0,0]
    curr=head

    while curr:
        count[curr.data]+=1
        curr=curr.next
    #NOTE: The counting part is done. It will be containing how many zeroes,ones and twos are there.

    curr=head
    for i in range(3):
        while count[i]>0:
            curr.data=i
            curr=curr.next
            count[i]-=1
    #NOTE: for loop runs across the three counters of 0s, 1s and 2s.
    # and then we have while loop, which runs till each counter becomes 0. and then we make the curr node value of that particular element counter.
    # and then decrement the counter as we insert the element one by one.
    #time complexity is O(N)
    return head


#TODO: this is the optimal solution for sorting list wiht values contains only 0s,1s and 2s.
#story: so we'll make three seperate LLs of each containing 0s,1s and 2s and then we'll join them together.


def optimal(head):
    if not head or not head.next:
        return head
    #NOTE: this are the pointers or references to head of each list.
    zero_head = Node(-1)
    one_head=Node(-1)
    two_head=Node(-1)
    #NOTE: these are used for traversing or inserting the new nodes.
    zero=zero_head
    one=one_head
    two=two_head

    curr=head
    while curr:
        #NOTE: check if the data is 0,1 or 2 and add the nodes accordingly.
        if curr.data == 0:
            zero.next=curr
            zero=zero.next
        elif curr.data == 1:
            one.next=curr
            one=one.next
        else:
            two.next=curr
            two=two.next
        curr=curr.next

    zero.next=one_head.next if one_head else two_head.next
    one.next = two_head.next
    two.next = None

    return zero_head.next









def create_linked_list(arr):
    head=Node(arr[0])
    curr=head
    for i in range(len(arr)):
        curr.next=Node(arr[i])
        curr=curr.next
    return head

def printLL(head):
    curr=head
    while curr:
        print(curr.data,end=" ")
        curr=curr.next
    print()

arr = [2,1,0,1,2,0,2,1]
head= create_linked_list(arr)
print("Original List: ")
printLL(head)

sorted_head= brute(head)
print("Sorted List:")
printLL(sorted_head)

sorted_head_opt = optimal(head)
print("Sorted List using optimal: ")
printLL(sorted_head_opt)
