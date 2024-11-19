#FIXME: the question is to return the starting point or node of the loop if it exists in the given linked list.
class Node:
    def __init__(self,data, next_node = None):
        self.data = data
        self.next = next_node

#TODO: brute force approach is to put all the nodes in a map, if the node is found again while traversing the linked list it is returned.
def brute_force(head):
    temp = head
    node_map = {}
    while temp is not None:
        if temp in node_map:
            return temp
        node_map[temp] = True
        temp = temp.next
    return None


def optimal_approach(head):
#TODO: this uses the same tortoise and hare approach:
    fast = head
    slow = head
    #TODO: same intuition as the return the middle node problem.
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        #TODO: if slow == fast. then we make slow as head, and move both the fast and slow by one node each time, when they meet that is the 
        #TODO: starting point of the loop.
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
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

# Detect the loop in the linked list
loop_start_node = brute_force(head)
if loop_start_node:
    print("Loop detected. Starting node of the loop is : ",loop_start_node.data)
else:
    print("No loop detected in the linked list.")
print("This is using optimal_approach hare and tortoise method.")
ans = optimal_approach(head)
if ans:
    print("Loop detected, starting node is ", ans.data)
else:
    print("Loop undetected.")

