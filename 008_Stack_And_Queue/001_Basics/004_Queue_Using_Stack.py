#FIXME: This is the same as before but instead we reverse the roles here. we are making a queue using stacks.
# classes under queue module: 1) Queue 2) LifoQueue 3) Priority Queue 4) simple queue
#TODO: Queue: A thread safe FIFO queue. gives enqueue and dequeue operations.
#NOTE: LifoQueue: A thread safe LIFO queue. same functions.
# PriorityQueue : A thread-safe queue that retrieves the entries in ascending order based on their Priority
# Simple Queue: unbounded FIFO queue without task tracking.

from queue import LifoQueue

class Queue:
    def __init__(self):
        self.input = LifoQueue()
        self.output= LifoQueue()

    def push(self,data):
        #TODO: so there are two queues here one is input and the other one is output.
        # So input is the actual LifoQueue used to push the elements into the queue. But output is used for actually transferring all the elements before and after the pushing of the elements.
        #NOTE: before pushing the give item into the input, we transfer all the elements in the input queue to the output queue. So now the input queue is empty.
        while not self.input.empty():
            self.output.put(self.input.get())
        print("The element pushed is ",data)
        #NOTE: Here we push the given element to the input queue, now the input queue only contains the only queue.
        self.input.put(data)
        #NOTE: Here we are again putting back all the elements back to the input elements so that the all the other elements are added after the given element.
        while not self.output.empty():
            self.input.put(self.output.get())


    def pop(self):
        if self.input.qsize() == 0:
            print("Stack is empty")
            exit(0)
        #NOTE: since the input queue is original queue , we do get() to that queue only.
        val=self.input.get()
        return val
    
    def Top(self):
        if self.input.qsize() == 0:
            print("Stack is empty")
            exit(0)
        return self.input.queue[-1]
    
    def size(self):
        return self.input.qsize()

if __name__ == "__main__":
    q = Queue()
    q.push(3)
    q.push(4)
    print("The element poped is", q.pop())
    q.push(5)
    print("The top of the queue is", q.Top())
    print("The size of the queue is", q.size())
