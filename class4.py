# pre define data type
# 1 int 
# 2 char
# 3 float
# 3 double
# 4 

#user define data type non-primitive

# class Student{

# }

# class Teacher{
    
# }

# class Employee{

# }

# class Book{
    
# }

# Using class key word we can create user define data types
# int=1,2,3,4,-2
# char='a','A','c'
# float=2.4,-4.6


# class Student:
#     def acceptdata(self,roll_no,name,city):
#         self.roll_no = 0
#         self.name=""
#         self.city=""
#         print("Student 3 details:")
#         print(roll_no)
#         print(name)
#         print(city)
# s1= Student()
# s2= Student()
# s3= Student()
# s3.acceptdata(1,"abc","hyd")
# s1.roll_no=101
# s1.name="John"
# s1.city="New York"
# print("Student 1 Details:")
# print("Roll No:",s1.roll_no)    
# print("Name:",s1.name)
# print("City:",s1.city)
# print("Stdent 3 Details:")
# print("Roll No:",s3.roll_no)6
# print("Name:",s3.name)
# print("City:",s3.city)



# class Student:
#     def acceptdata(self):
#         self.roll_no = int(input("Enter roll no:"))
#         self.name=input("Enter name:")
#     def showData(self):
#         print("Roll No:",self.roll_no)
#         print("Name:",self.name)
# s1= Student()
# s1.acceptdata()
# s1.showData()
# s2= Student()
# s2.acceptdata()
# s2.showData()


# class Student:
#     college_name="ABC College"
#     def acceptdata(self):
#         self.name=input("Enter name:")
#         self.m1=float(input("Enter marks1:"))
#         self.m2=float(input("Enter marks2:"))
#         self.m3=float(input("Enter marks3:"))
#     def showData(self):
#         total=self.m1+self.m2+self.m3
#         percentage=(total/300)*100
#         print("Name:",self.name)
#         print("College Name:",Student.college_name)
#         print("Total Marks:",total)
#         print("Percentage:",percentage)
# s1= Student()
# s1.acceptdata()
# s1.showData()


#constructor 
# class Student:
#     def msg(self):
#         print("Hello Students")
# s= Student()
# s.msg()


# class Student:
#     def __init__(self):#constructor (__init__)
#         print("Hello Students")
# s= Student()


class Student:
    def __init__(self):
        pass
    def msg(self):
        print("Hello Students")
s= Student()
s.msg()


class Student:
    def __init__(self):
        self.name="John"
        self.age=101
    def display(self):
        print(f"Name:{self.name} age:{self.age}")
s= Student()
s.display()


class car:
    def __init__(self):
        self.name="BMW"
        self.model="X5"
    def display(self):
        print(f"Car Name:{self.name} Model:{self.model}")
c= car()
c.display()


# parameterized constructor
class Student:
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name
s1= Student(101,"John")
print(s1.roll,s1.name)


class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
c1= Car("Toyota","Camry",2020)
print(c1.brand,c1.model,c1.year)


#distructor 
class Employee:
    def __init__(self):
        print("Employee Object Created")
    def __del__(self):
        print("distructor clled, Employee Object Deleted")
e1= Employee()
del e1


#inheritance 
class A:
    a=10
class B(A):
    def display(self):
        print(self.a)
b1= B()
b1.display()


class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
d1= Dog()
d1.speak()
d1.bark()


#multilevel inheritance
class grandfather:
    def show_grandfather(self):
        print("I am grandfather")
class father(grandfather):
    def show_father(self):
        print("I am father")
class son(father):
    def show_son(self):
        print("I am son")
s1= son()
s1.show_grandfather()   
s1.show_father()
s1.show_son()


class Person:
    def name(self):
        print("I am a person")
class Employee(Person):
    def salary(self):
        print("200,000 per annum")
class Manager(Employee):
    def role(self):
        print("Sales Department")
m1= Manager()
m1.name()
m1.salary()
m1.role()


#multiple inheritance 

class Father:
    def skills(self):
        print("Father: Gardening,working")
class Mother:
    def hobbies(self):
        print("Mother: Cooking,painting")
class Child(Father,Mother):
    def play(self):
        print("Child: Gaming,sports")
c1= Child()
c1.skills()
c1.hobbies()
c1.play()


# hierarchical inheritance
class Parent:
    def show_parent(self):
        print("I am parent")
class Child1(Parent):
    def show_child1(self):
        print("I am child 1")
class Child2(Parent):
    def show_child2(self):
        print("I am child 2")
c1= Child1()
c1.show_parent()
c1.show_child1()
c2= Child2()
c2.show_parent()
c2.show_child2()

# hybrid inheritance
class A:
    def a(self):
        print("a")
class B(A):
    def b(self):
        print("b")
class C(A):
    def c(self):
        print("c")
class D(B,C):
    def d(self):
        print("d") 
d1= D()
d1.a()
d1.b()
d1.c()
d1.d()


#method overriding 
#same name& same parameter
class Parent:
    def show(self):
        print("this is parent class method")
class Child(Parent):
    def show(self):
        # call parent implementation first
        super().show()
        print("this is child class method")

c1= Child()
c1.show()

#encapsulation
#class=methods+variables 
class Student:
    def __init__(self,name,marks):
        self.__marks=marks #private variable
        self.name=name
    def show(self):
            print("Name:",self.name)
            print("Marks:",self.__marks)
    def set_marks(self,marks):
        if marks>=0 : 
            self.__marks=marks
s1= Student("John",6)
s1.show()
s1.set_marks(-4)
s1.show()

#Encapsulation is the process of binding data and methods together
#and restricting dicrect access to data


#polymorphism
#same name different behavior
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cat meows")

#polymorphic
animal=[Animal(),Dog(),Cat()]
for a in animal:
    a.sound()


#dunder methods __init__
# __str__ decides what to show when we print an object
class Student:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
s1= Student("John")
print(s1)


class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def __str__(self):
        return self.name + " has balance: " + str(self.balance)
account= BankAccount("Alice",1000)
print(account)

#__len__ used when len() function is called
class Mydata:
    def __init__(self,data):
        self.data=data
    def __len__(self):
        return len(self.data)
d1= Mydata([1,2,3])
print(len(d1))

#__add__ (+)
class Number:
    def __init__(self,x):
        self.x=x
    def __add__(self,n2):
        return self.x + n2.x
n1= Number(5)
n2= Number(10)
print(n1 + n2)

#__sub__ (-)
class Number:
    def __init__(self,x):
        self.x=x
    def __sub__(self,n2):
        return self.x - n2.x
n1= Number(15)
n2= Number(5)
print(n1 - n2)

#__truediv__ (/)
class Number:
    def __init__(self,x):
        self.x=x
    def __truediv__(self,n2):
        return self.x / n2.x
n1= Number(20)
n2= Number(4)
print(n1 / n2)

#__mul__ (*)
class Number:
    def __init__(self,x):
        self.x=x
    def __mul__(self,n2):
        return self.x * n2.x
n1= Number(3)
n2= Number(7)
print(n1 * n2)

#__eq__ (==)
class Number:
    def __init__(self,x):
        self.x=x
    def __eq__(self,n2):
        return self.x == n2.x  
n1= Number(5)
n2= Number(5)
print(n1 == n2)

#__lt__ (<)
class Number:
    def __init__(self,x):
        self.x=x
    def __lt__(self,n2):
        return self.x < n2.x
n1= Number(3)
n2= Number(7)
print(n1 < n2)


