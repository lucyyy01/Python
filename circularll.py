class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Circularlinkedlist:
    head=None
    def Insertatlast(self):
        if self.head==None:
            self.head=Node(int(input("Enter data:")))
            self.head.next=self.head
        else:
            t=self.head
            while t.next!=self.head:
                t=t.next
            t.next=Node(int(input("Enter data:")))
            t.next.next=self.head
    # def display(self):
    #     if self.head==None:
    #         print("No node")
    #     else:
    #         t=self.head
    #         while t.next!=self.head:
    #             print(t.data,end=" ")
    #             t=t.next
    #         print(t.data)
    def display(self):
        t=self.head
        if self.head==None:
            print("No node")
        else:
            while True:
                print(t.data,end=" ")
                t=t.next
                if t==self.head:
                    break
    def Insertatfirst(self):
        if self.head==None:
            self.head=Node(int(input("Enter data:")))
            self.head.next=self.head
        else:
            t=self.head
            self.head=Node(int(input("Enter data:")))
            self.head.next=t
            while t.next!=self.head.next:
                t=t.next
            t.next=self.head
    def countnode(self):
        t=self.head
        if self.head==None:
            print("No node")
        else:
            count=0
            while True:
                t=t.next
                count+=1
                if t==self.head:
                    break
            print(count)
    # def insertatposition(self):
    #     if self.head==None:
    #         self.head=Node(int(input("Enter data:")))
    #         self.head=self.head
    #     else:
    #         t=t.next
    #         p=int(input("Enter position:"))
    #         for i in range(1,p):
    def deletefirstnode(self):
        if self.head.next==self.head:
            self.head=None
        else:
            t=self.head
            while t.next!=self.head:
                t=t.next
            self.head=self.head.next
            t.next=self.head

c=Circularlinkedlist()
c.Insertatlast()
c.Insertatlast() 
c.Insertatlast() 
c.Insertatlast()
c.Insertatfirst() 
c.Insertatfirst() 
c.Insertatfirst() 
c.countnode()
# print(c.head.data)
# print(c.head.next.data)
c.display()