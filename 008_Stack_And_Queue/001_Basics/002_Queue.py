#TODO: Implementation of Queue using arrays.

class Queue:
    def __init__(self):
        self.start=-1
        self.end=-1
        self.currSize=0
        self.maxSize=16
        self.arr=[0]*self.maxSize

def push(self,x:int)->None:
    if self.currSize == self.maxSize:
        print("Queue is full\nExiting...")
        exit(1)
    if self.end==-1:
        self.start=0
        self.end=0
    else:
        self.end=(self.end+1)%self.maxSize
    self.arr[self.end]=x
    self.currSize+=1
