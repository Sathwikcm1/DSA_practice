#FIXME: The problem : we have to return the middle node of the given linked list. for ex: 1,2,3,4,5 return 3, 
#if not , 1,2,3,4,5,6 , return 4. the greater element must be returned when the length is even.
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next=next


#TODO: this is the brute_force_approach of this problem. 
#story: to return the middle node of the linked list, we have to count the how many nodes are there in the list.
# and then calculate the middle node, mid = count//2 + 1, +1 is because we have to return the greater part, and then again traverse the LL.
# and when we find the middle node we return it.
def brute_force_approach(head):
    #NOTE: if the head is empty return head.
    if head is None or head.next is None:
        return head
    
    temp = head
    cnt = 0 #NOTE: if you take count as 0, you have to increment it before temp=temp.next
    
    while temp:
        cnt+=1
        temp = temp.next
    #NOTE: now , temp will be pointing to Null, we just traversed linked list to find out the lenght of the linked list.
    mid = cnt // 2 + 1
    #NOTE: calculating the mid value and reinitialising the temp value is important.
    temp = head
    while temp:
        mid = mid -1 
        if mid == 0:
            break
        temp = temp.next
    #NOTE: now temp will be pointing to the mid node only so we can return temp node
    return temp
#NOTE: time complexity: this will take, O(N) + O(N/2).




#TODO: this is optimal_approach of this problem.
#this will use the famous algorithm known as tortoise and hare method.
#story: the fast pointer will move by two nodes and slow will move by one node.
#Time complexity is O(N).


def optimal_approach(head):
    slow = head
    fast = head

    while fast and fast.next and slow:
        fast = fast.next.next
        slow = slow.next
    return slow


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

ans1 = brute_force_approach(head)
print("The middle node of the linked list is : ", ans1.data)
