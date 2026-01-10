class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Singlylinkedlist:
    def __init__(self):
        self.head=None
    def Insertatfirst(self):
        n=Node(int(input("Enter data:")))
        n.next=self.head
        self.head=n
    def Insertatlast(self):
        if self.head==None:
            self.head=Node(int(input("Enter data:")))
        else:
            t=self.head
            while t.next!=None:
                t=t.next
            t.next=Node(int(input("Enter data:")))
    def deleteatfirst(self):
        if self.head==None:
            print("No node")
        else:
            temp=self.head
            self.head=self.head.next
            temp=None
    def display(self):
        t=self.head
        if t==None:
            print("No node available")
        else:
            while t:
                print(t.data,end=" ")
                t=t.next
    def searchNode(self):
        t=self.head
        n=int(input("Enter data to search:"))
        countIndex=1
        if t==None:
            print("No node available")
        else:
            while t!=n:
                if n==t.data:
                    print("Index of data is:",countIndex)
                    return
                else:
                    countIndex+=1   
                    t=t.next   
    def EvenSum(self):
        t=self.head
        if t==None:
            print("No node available")
        else:
            sum=0
            while t!=None:
                if t.data%2==0:
                    sum+=t.data
                t=t.next
            print("Sum of even number is:",sum)

s=Singlylinkedlist()
s.Insertatfirst()
s.Insertatfirst()
s.Insertatfirst()
s.Insertatlast()
s.Insertatlast()
s.Insertatlast()
s.display()
s.searchNode()
s.EvenSum()

