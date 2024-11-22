#FIXME: We have to remove Nth node from the back of a linked list.
# for example 1->2->3->4->4=>5, and n = 2 so the output would be 1->2->3->4->5
class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

#TODO: this is the brute force approach.
# story: so first we will count the no of nodes in the linked list.
# and then we will subtract the cnt by number. now we have to traverse to that particular result and delete that node.

def brute_force(head,N):
    if head is None:
        return None
    cnt = 0
    temp = head

    while temp:
        cnt+=1
        temp=temp.next
    #NOTE: this is the case, where N is the first node, so we delete head and return the next node to the head.
    if cnt == N:
        new_head = head.next
        head=None
        return new_head
    
    res = cnt-N
    temp = head
    while temp:
        res-=1
        if res == 0:
            break
        temp=temp.next
    delNode = temp.next
    temp.next = temp.next.next
    delNode = None
    return head

def printLL(head):
    while head:
        print(head.val,end = " ")
        head=head.next
    print()


#TODO:this is the optimised version of the above brute force which uses the same hare and tortoise algorithm.
#Story:two pointers fast and slow, first the fast pointer is moved "N" nodes from the head. And then they both start moving with the same pace until fast reaches end of list. 
#when it reaches the end of the list slow pointer is n nodes behind fast, which is exactly what we wanted we can then delete that node.
def optimal_approach(head,N):
    fast = head
    slow = head
    for i in range(N):
        fast = fast.next
    #NOTE:if the N is the size of the list, delete the head and return the rest of the list.

    if fast is None:
        return head.next
    while fast.next :
        fast=fast.next
        slow=slow.next

    delNode=slow.next
    slow.next=slow.next.next
    delNode=None
    return head



arr = [1, 2, 3, 4, 5]
N = 3
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])
head.next.next.next.next = Node(arr[4])

print("Original List:")
printLL(head)
print("After altering:")
head = brute_force(head,N)
printLL(head)

print("Before optimal deletion:")
printLL(head)
print("After optimal deletion:")
head = optimal_approach(head,N)
printLL(head)
