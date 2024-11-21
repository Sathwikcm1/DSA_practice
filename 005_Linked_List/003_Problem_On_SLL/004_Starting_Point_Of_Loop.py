#FIXME: we have to return the starting node of the loop in a linked list if a loop exists.

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

#TODO: this is the brute force approach.
#story: adding every node into a boolean dictionary while also checking if the current node is already in the dictionary or not.

def brute_force_approach(head):
    bin_dict = {}
    #NOTE: initialising the dictionary.
    temp = head
    #NOTE: can also use set instead of dictionary it is not obligatory that we have to use dictionary here.
    while temp:
        #NOTE: checking if the current node is already in the dictionary or not.
        if temp in bin_dict:
            return temp
        bin_dict[temp] = True
        temp = temp.next
    return None

#TODO: Takes the time complexity of O(N).


#TODO: This is the optimal solution of this problem.
# using the same good old hare tortoise method.

def optimal_approach(head):
    slow=head
    fast=head

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

        if slow == fast:
            slow=head
            while slow != fast:
                slow =slow.next
                fast=fast.next
            return slow #TODO: or even return fast both will be pointing to the same node.
    return None







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

brute = brute_force_approach(head)
if brute:
    print("Loop detected, Starting of the loop is ",brute.data)
else:
    print("No loop detected.")
