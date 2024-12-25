#FIXME: This question is basically implementing stacks but using queues from module queue and class Queue.
#TODO: This is where we import the queue module and in that particulary Queue class.
# so the queue module contains several classes that implement different types of queue datastructures.
# The first one is Queue, FIFO principle, Tread safe(meaning it can be used safely in multi threaded programming), methods are put(item), get(), empty(), full() and qsize().
# The second one  is LifoQueue(LIFO) also thread safe. Methods are similar to Queue.
# The third one is Priority Queue, A queue where items are retrieved in priority order(lowest by default).
# Other important modules for DSA: collections(deque,counter,defaultdict), heapq, bisect, array, math random, itertools etc.
from queue import Queue

class Mystack:
    def __init__(self):
        self.q=Queue() #NOTE: creating an object of Queue. Queue doesn't allow indexing, it allows provides secure method to put and get the values into the queue.

    def push(self,e):
        s=self.q.qsize() #NOTE: This will give size of the current queue. qsize() will give that.
        self.q.put(e)
        for _ in range(s):
            self.q.put(self.q.get())

    def pop(self):
        n=self.q.get()
        return n 
    def top(self):
        return self.q.queue[0]
    def empty(self):
        return self.q.qsize() == 0

st = Mystack()
st.push(10)
st.push(20)
st.push(30)
print("The top of the stack is ",st.top())
print("The popped element is ",st.pop())
print("Now the top element in the stack is ",st.top())
