#FIXME: The question is to find the intersection point between two linked lists.
# example : 1-> 2-> 3-> 4 -> 5, 7->4->5, these two are intersection point at node 4 so we should return node 4. returning the node itself not the index.

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def insertNode(head,val):
    newNode=Node(val)
    if head == None:
        head=newNode
        return head
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=newNode
    return head


def printList(head):
    while head:
        print(head.val,end=" ")
        head=head.next
    print()

#TODO: this is the brute force solution for this problem.
#story: so to find the intersection point between these two linked list.
#we take two heads, head1 and head2 we make two loops inside one another, we will check for each node.
#And whenever we find the same node, we just return that node.

def brute(head1,head2):
    while head2:
        temp=head1
        while temp:
            if temp==head2:
                return head2
            temp=temp.next
        head2=head2.next
    return None


#TODO: this is brute force solution 2, this uses hashmap technique but using set.
def brute_two(head1,head2):
    st = set()
    while head1:
        st.add(head1)
        head1=head1.next
    while head2:
        if head2 in st:
            return head2
        head2=head2.next
    return None




#TODO:: This optimal way to do it.
#story: we will have two pointers p1 and p2 pointing to heads of each linked lists respectively.
# and then when one of them becomes None we make it point to the head of the other linked list.
# until they meet each other when they do they will be standing on the intersection point.
# NOTE: the total distance travelled by both the pointers equalize when they switch lists.
# This ensures that they meet at the intersection nodes.
def optimal(head1,head2):
    p1=head1
    p2=head2
    while p1!=p2:
        p1=head2 if p1 is None else p1.next
        p2=head1 if p2 is None else p2.next

    return p1




if __name__ == '__main__':
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 3)
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 4)
    head1 = head
    head = head.next.next.next
    headSec = None
    headSec = insertNode(headSec, 3)
    head2 = headSec
    headSec.next = head
    print('List1: ', end='')
    printList(head1)
    print('List2: ', end='')
    printList(head2)
    answerNode = brute(head1, head2)
    if answerNode == None:
        print('No intersection')
    else:
        print('The intersection point is', answerNode.val)

    answer2 = optimal(head1,head2)
    if not answer2:
        print("No Intersection.")
    else:
        print("The intersection Point is using optimal:",answer2.val)



