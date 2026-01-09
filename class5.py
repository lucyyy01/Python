# #palindrome number
# # num = int(input("Enter a number: "))
# # temp = num
# # rev = 0
# # while num > 0:
# #     digit = num % 10
# #     rev = rev * 10 + digit
# #     num = num // 10
# # if temp == rev:
# #     print(f"{temp} is a palindrome number")
# # else:
# #     print(f"{temp} is not a palindrome number")

# #palindrome using string
# # str1 = input("Enter a string: ")
# # str1=str(str1)
# # rev_str = str[::-1]
# # if str1 == rev_str:
# #     print(f'"{str1}" is a palindrome string')
# # else:
# #     print(f'"{str1}" is not a palindrome string')


# #armstrong number
# # num=int(input("Enter number :"))
# # temp=num
# # sum=0
# # n=len(str(temp))
# # while num>0:
# #     digit=num%10
# #     sum+=digit**n
# #     num=num//10
# # if temp==sum:
# #     print("Number is armstrong number")
# # else:
# #     print("Number is not armtrong number")


# #Linked list
# # class Node:
# #     a=2
# #     def CreateMember(self):
# #         data=8
# # n1=Node()
# # n1.CreateMember()
# # print(n1.data) #error


# # class Node:
# #     a=2
# #     def CreateMember(self):
# #         self.data=8
# # n1=Node()
# # n1.CreateMember()
# # print(n1.data) #8



# class Node:
#     def createmember(self):
#         self.data=8
# n1=Node()
# n1.createmember()
# print(n1.data)


# class Node:
#     def createmember(self):
#         self.data=8
#         self.next=None
# n1=Node()
# n1.createmember()
# print(n1.data)


# class Node:
#     def fun1(self):
#         self.x=50
#     def fun2(self):
#         self.y=40
# n1=Node()
# n1.fun1()
# n1.fun2()
# print(n1.x)
# print(n1.y)


# class Node:
#     def createmember(self):
#         self.data=8
#         self.next=None
# n1=Node()
# n1.createmember()
# print(n1.data)


# # class Node:
# #     def createmember(self):
# #         self.data=int(input("Enter number:"))
# #         self.next=None
# # n1=Node()
# # n1.createmember()
# # print(n1.data)
# # n2=Node()
# # n2.createmember()
# # print(n2.data)


# class Node():
#     def createmember(self,d):
#         self.data=d
#         self.next=None
# n1=Node()
# n2=Node()
# n1.createmember(5)
# n2.createmember(10)
# print(n1.data,n2.data)

# class Node:
#     def createmember(self,data):
#         self.data=data
#         self.next=None
# n1=Node()
# n2=Node()
# n1.createmember(6)
# n2.createmember(8)
# print(n1.data,n2.data)


# class Node:
#     def createmember(self,data,next=None):
#         self.data=data
#         self.next=next
# n1=Node()
# n2=Node()
# n1.createmember(6)
# n2.createmember(9)
# print(n1.data,n2.data)


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# n1=Node(5)
# n2=Node(10)
# n3=Node(15)
# print(n1.data)
# print(n2.data)
# print(n3.data)


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# n1=Node(6)
# n2=Node(10)
# n3=Node(15)

# n1.next=n2
# n2.next=n3

# print(n1.data)
# print(n1.next.data)
# print(n1.next.next.data)


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# n1=Node(5)
# n2=Node(10)
# n3=Node(15)

# n1.next=n2
# n2.next=n3

# t=n1

# while t!=None:
#     print(t.data,end=" ")
#     t=t.next


# class Node():
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# n1=Node(1)
# n2=Node(2)
# n3=Node(3)
# n4=Node(4)
# n5=Node(5)
 
# n1.next=n2
# n2.next=n3
# n3.next=n4
# n4.next=n5

# t=n1

# while t!=None:
#     print(t.data,end=" ")
#     t=t.next


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def InsertAtFirst(self):
        n=Node(int(input("Enter data:")))
        n.next=self.head
        self.head=n
    def InsertNodeAtLast(self):
        if self.head==None:
            d=int(input("Enter data:"))
            self.head=Node(d)
        else:
            t=self.head
            while t.next!=None:
                t=t.next
            t.next=Node(int(input("Enter data:")))
    def delectatfirst(self):
        if self.head==None:
            print("No node")
        else:
            temp=self.head
            self.head=self.head.next
            temp=None
    def deleteatlast(self):
        if self.head==None:
            print("No node")
        else:
            temp=self.head
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None
    def Countnode(self):
        if self.head==None:
            print("No node")
        else:
            count=0
            t=self.head
            while t:
                t=t.next
                count+=1
            print(count)
    def sum(self):
        if self.head==None:
            print("No node")
        else:
            sum=0
            t=self.head
            while t:
                sum+=t.data
                t=t.next
            print(sum)
    def min(self):
        if self.head==None:
            print("No node")
        else:
            t=self.head.data
            temp=self.head
            while temp:
                if t>temp.data:
                    t=temp.data
                temp=temp.next
            print(t)
    def max(self):
        if self.head==None:
            print("No node")
        else:
            t=self.head.data
            temp=self.head
            while temp:
                if t<temp.data:
                    t=temp.data
                temp=temp.next
            print(t)
    def even(self):
        if self.head==None:
            print("No node")
        else:
            t=self.head
            while t:
                if t.data%2==0:
                    print(t.data,end=" ")
                t=t.next
            print("\n")
    def display(self):
        t=self.head
        if t==None:
            print("No node available")
        else:
            while t:
                print(t.data,end=" ")
                t=t.next

s=SinglyLinkedList()
s.InsertAtFirst()
s.InsertAtFirst()
s.InsertAtFirst()
s.InsertNodeAtLast()
s.InsertNodeAtLast()
s.InsertNodeAtLast()
s.delectatfirst()
s.deleteatlast()
s.Countnode()
s.sum()
s.min()
s.max()
s.even()
s.display()

