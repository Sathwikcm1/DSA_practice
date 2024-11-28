#FIXME: The given linked list's node will have three things data, next and child.
# some of the nodes will have child linked list. we have to arrange all of these nodes including child in a single linked list that is sorted.
# example: List:
"""
List:
1 -> 3 -> 4
    |
    2 -> 6
"""
#will become : 
"""
1 -> 2 -> 3 -> 4 -> 6
"""
class Node:
    def __init__(self,val,next=None,child=None):
        self.val=val
        self.next=next
        self.child=child

#TODO: Story: we will take the value of each node and put it in an array and then sort the array and make a clean linked list out of out and return that new linked list.
def flattenLL(head):
    if not head:
        return None
    nodes=[] #NOTE: this will have all the node values including child nodes.
    def extractNodes(node):
        while node:
            nodes.append(node.val)
            if node.child:
                extractNodes(node.child)
            node=node.next

    extractNodes(head)


    nodes.sort()
    dmy=Node(0)
    curr=dmy 
    for val in nodes:
        curr.next=Node(val)
        curr=curr.next
    return dmy.next

def main():
    head=Node(1)
    head.next=Node(3)
    head.next.next=Node(4)
    head.child = Node(2)
    head.child.next=Node(6)

    flatten_head=flattenLL(head)

    curr=flatten_head
    print("The Sorted Linked List:")
    while curr:
        print(curr.val,end=" " if curr.next else "\n")
        curr=curr.next

if __name__ == "__main__":
    main()

