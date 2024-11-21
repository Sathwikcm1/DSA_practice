#FIXME: The question is to return true if there is a loop in the given linked list otherwise return Falsee.

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

#TODO: This is the brute_force_approach:
#story: we will check if the loop is present , if the same node it self is repeated twice.
# so we go on adding nodes to node_set, while adding we also check if the current is already present in the set or not if it is we return True.
def brute_force_approach(head):
    temp = head
    #NOTE: initialising the set i know quite wierd but it is what it is.
    node_set = set()

    while temp:
        #NOTE: check if the node in already in the list or not.
        if temp in node_set:
            return True 
        
        node_set.add(temp)
        temp=temp.next
    return False 
#TODO: the time complexity is O(N * 2 * log(N)).
# the O(n) comes from traversing the list and 2*log(N) for insertion and searchign in unordered_set.




#TODO: this is the optimal solution: this will take O(N) time complexity.
# Again this is the same hare tortoise solution. a slow pointer and a fast pointer.
# story: we use the same fast and slow pointers, while traversing if fast == slow, then we can say that the give linked list has a cycle in it.
def optimal_approach(head):
    slow = head
    fast = head

    #NOTE: fast.next , we check this for even number of nodes.
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            return True
    return False
#TODO: what makes one say that they will meet together, since the fast is two steps ahead eventally it will catch up to slow.


head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
    # Create a loop
fifth.next = third


if brute_force_approach(head):
    print("The loop is present in the given linked list.")
else:
    print("The loop is not present in the given linked list.")

if optimal_approach(head):
    print("This is using optimal_approach , loop is present.")
else:
    print("There ain't no goddamn loop.")
