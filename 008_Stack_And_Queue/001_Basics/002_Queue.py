#TODO: Implementatation of Queues using arrays.

class Queue:
    def __init__(self,capacity=1000):
        self.front=0 #NOTE: pointer that points to the starting of the queue.
        self.rear=-1 #NOTE: pointer that points to the ending of the queue.
        self.size=0 #NOTE: Current size of the queue.
        self.capacity=capacity #NOTE: capacity is actual data structure of the queue, inside which this queue exists.
        self.arr = [0] * capacity

    def enqueue(self,item):
        if self.is_full():
            print("Queue Overflow.")
            return 
        self.rear=(self.rear + 1) % self.capacity #NOTE: this is because at the end of the queue wraps around
        #NOTE: so doing modulus would bring the rear to the front of the queue which can be used to insert more elements.
        self.arr[self.rear]=item
        self.size+=1 

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow.")
            return -1
        item=self.arr[self.front]
        self.front=(self.front+1) % self.capacity
        self.size-=1 
        return item
    
    def peek(self):
        if self.is_empty():
            print("The queue is empty.")
            return -1
        return self.arr[self.front]

    def is_empty(self):
        if self.size==0:
            return True
        else:
            return False
    def is_full(self):
        if self.size == self.capacity:
            return True
   

    def current_size(self):
        return self.size



if __name__ == "__main__":
    q = Queue(5)  # Create a queue with capacity 5
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Front element is:", q.peek())  # Output: 10
    print("Queue size is:", q.current_size())  # Output: 3

    print("Dequeued element:", q.dequeue())  # Output: 10
    print("Front element is now:", q.peek())  # Output: 20
    print("Queue size after dequeue:", q.current_size())  # Output: 2

    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)

    print("Is the queue full?", q.is_full())  # Output: True

    q.enqueue(70)  # This will print "Queue Overflow."

