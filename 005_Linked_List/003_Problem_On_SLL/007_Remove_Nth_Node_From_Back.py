#FIXME: We have to remove Nth node from the back of a linked list.
# for example 1->2->3->4->4=>5, and n = 2 so the output would be 1->2->3->4->5
class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

#TODO: this is the brute force approach.
