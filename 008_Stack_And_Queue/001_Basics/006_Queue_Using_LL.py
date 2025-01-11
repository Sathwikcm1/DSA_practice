#FIXME: This question is basically forming a queue that is based of linked list.
#since queue follows first in first out principle, we gotta figure out the part the where it should have to pop the element in the front .

#TODO: a class for a linked list node.
class queueNode():
    def __init__(self,data=None):
        self.val = data
        self.next = None


#TODO: This is class is for actually for
class Queue:
    def __init__(self):
        self.front = None #NOTE: front pointer that points to the front element of the queue.
        self.rear = None #NOTE: Rear pointer that points to the rear element of the queue.
        self.size = 0 #NOTE: keep track of the size of queue.
    
    def is_empty(self):
        return self.front is None

    def enqueue(self,value): #NOTE: This is pushing elements into the queue. 
        temp = queueNode(value) #NOTE: create a node for queue.
        if self.front is None: #NOTE: if the first node itself is null, then we add both rear and front pointers are pointing to the same element is current temp.
            self.front = temp
            self.rear = temp
        else:
            self.rear.next = temp #NOTE: making the previous node next pointer to the current node.
            self.rear = temp #TODO: moving the rear to the current node in the queue.
        print(f"{value} Inserted into the Queue.")
        self.size += 1


    def dequeue(self): #TODO: Function to pop element from the front of the queue.
        if self.front is None: #NOTE: if the front of the queue is empty then it means that the queue is empty.
            print("The queue is already empty.")
        else:
            print(f"{self.front.val} Removed from queue.") #NOTE: printing the front element of the queue.
            temp = self.front.val #NOTE: putting the value for it to be returned. 
            self.front = self.front.next
            self.size -= 1 #NOTE: decrement the size of the queue.
            return temp
            del temp

    def peek(self):
        if self.is_empty():
            print("The queue is empty.")
            return -1
        else:
            return self.front.val

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    print(f"The size of the Queue is {q.size}.")
    print(f"The peek of elements of the queue is {q.peek()}")
    popped_el = q.dequeue()
    print(f"The Popped element at the end after pushing everything, it should be 10 , but is {popped_el} .")

