class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def Push(self):
        n=Node(int(input("Enter data:")))
        n.next=self.head
        self.head=n
    def Pop(self):
        t=self.head
        if t==None:
            print("No node")
        else:
            while t.next.next!=None:
                t=t.next
            t.next=None
    def Peek(self):
        if self.head==None:
            print("No node")
        else:
            print(self.head.data)
    def display(self):
        t=self.head
        if t==None:
            print("No node")
        else:
            while t:
                print(t.data,end=" ")
                t=t.next
            print("\n")
s=Stack()
s.Push()
s.Push()
s.Push()
s.Push()
s.display()
s.Peek()
        