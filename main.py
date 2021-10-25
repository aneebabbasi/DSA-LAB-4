#1st Task
import numpy as np
class queue:
  def _init_ (self):
    self.list=np.arange(3)
  def enqueue(self, data):
    e=np.append(self.list, data)
    return e
  def dequeue(self):
    d=np.delete((self.list,1))
    return d
  def front(self):
    f=self.list[0]
    return f
  def rear(self):
    r=self.list[-1]
    return r
  def length(self):
    l=len(self.list)
    return l
  def size(self):
    s=(len(self.list>5))
    return s
  def isEmpty(self):
    i=(len(selflist)==0)
    return i
  def main():
  q=queue()
    print(q)
#2nd Task
from collections import deque
class Deque:
    def _init_(self):
        self.items = []
    def isEmpty(self):
        e=self.items == []
        return e
    def addRear(self, item):
        ar=self.items.append(item)
        return ar
    def addFront(self, item):
        af=self.items.insert(0, item)
        return af
    def removeFront(self):
        rf=self.items.pop(0)
        return rf
    def removeRear(self):
        rr=self.items.pop()
        return rr
    def size(self):
        return len(self.items)
def main():
  q=Queue()
  print(q)


