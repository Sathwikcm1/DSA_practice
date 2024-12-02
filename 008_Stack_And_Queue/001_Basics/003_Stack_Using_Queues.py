#FIXME: This question is basically implementing stacks but using queues from module queue and class Queue.
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
