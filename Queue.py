class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
    def Enqueue(self):
        if self.head==None:
            d=int(input("Enter data:"))
            self.head=Node(d)
        else:
            t=self.head
            while t.next!=None:
                t=t.next
            t.next=Node(int(input("Enter data:")))
    def Dequeue(self):
        if self.head==None:
            print("No node")
        else:
            temp=self.head
            self.head=self.head.next
            temp=None
    def Peek(self):
        if self.head==None:
            print("No node")
        else:
            t=self.head
            while t.next !=None:
                t=t.next
            print(t.data)
    def display(self):
        if self.head==None:
            print("No node")
        else:
            t=self.head
            while t:
                print(t.data,end=" ")
                t=t.next
s=Queue()
s.Enqueue()
s.Enqueue()
s.Enqueue()
s.Dequeue()
s.display()
s.Peek()