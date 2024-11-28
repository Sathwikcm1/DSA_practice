#FIXME: simply reversing a doubly linked list and returning the new head.
class Node:
    def __init__(self,prev=None,val=0,next=None):
        self.prev=prev
        self.val=val
        self.next=next

def arr2DLL(arr):
    if not arr:
        return None
    head=Node(None,arr[0],None)
    prev=head

    for i in range(1,len(arr)):
        curr=Node(prev,arr[i],None)
        prev.next=curr
        prev=curr
    return head

def printLL(head):
    while head:
        print(head.val,end=" ")
        head=head.next
    print()

def reverse_DLL(head):
    if not head:
        return None
    temp=None
    curr=head

    while curr:
        temp=curr.prev
        curr.prev=curr.next
        curr.next=temp
        curr=curr.prev
    return temp.prev if temp else None

if __name__ == "__main__":
    arr=[1,2,3,4,5,6,7]
    head=arr2DLL(arr)
    print("Original List: ")
    printLL(head)

    print("After reversing the list: ")
    head=reverse_DLL(head)
    printLL(head)



