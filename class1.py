x,y,z=10,20,30
print(x)
print(x,y,z)
x=y=z="sbj"
print(x,y,z)

x=10

del x  # delete variable

name=input()
print (name)

name=input("enter name")
print(name)

name=input("enter name")
print("Your name is ",+name) # + & , is concatination

age=input("enter age")
print("your age is "+age)

#input() data type is always string

#type casting
age=int(input("enter age"))
print("your age is:",age)  # + is use to concatinate only strings 

age=int(input("enter age"))
print("your age is:"+str(age))  #convert 

def msg():
    """this function print msg hello"""
    print("Hello")

msg()
print(msg.__doc__)
print(len.__doc__)

#Data type
#Numeric  int float complex
x=10
print(x)

y=2e3
print(y)#2000.0

z=complex()
print(z)#0j
z=complex(5)
print(z)#5+0j
z=complex(5,6)
print(z)#5+6j
print(z.real)#5.0
print(z.imag)#6.0

#squence  string list tuple range
x="hello"
print(x)

li=[1,2,3,"hello"]#list is a ordered collection of elements 
#mutable means can be change 
# allow duplicate value 
#support indexing & slicing
li.append(4) #add  output-> 1 2 3 hello 4
print(li)
print(li[1])#output->1   indexing
print(li[4])#output->hello      indexing
print(li[0:2])#output->1 2 3     slicing

#tuple
#ordered collection of elements
#immutable
#allows  duplicates
#support indexing & slicing

t=(1,2,3,"hello",2)
print(t)
print(t[0])
print(t[0:3])

#range
# sequence of number
r=range(5)
print(r) #range(0,5)
print(list(r))#[0,1,2,3,4,5]
r=range(1,10)
print(list(r))#[1,2,3,4,5,6,7,8,9]  stops at -1 position
r=range(1,11)
print(list(r))#[1,2,3,4,5,6,7,8,9,10]
r=range(1,11,2) 
print(list(r))#[1,3,5,7,9]
r=range(10,0,-1)
print(list(r))



#set -> set   frozenset  
# unorderd collection of unique element-> duplicates not allowed
# mutable
#no indexing & slicing
s={1,2,3,4,5}
print(s)#output->{1,2,3,4,5}
#frozenset
# unorderd collection of unique element-> duplicates not allowed
# immutable
#no indexing & slicing
fs=frozenset({1,2,3,4,5})
print(fs)#frozenset({1,2,3,4,5})
vowels={'a','e','o','u'}
print(vowels)#{'a','e','o','u'}
fset=frozenset(vowels)
print(fset)#frozenset(vowels)

#mapping
#(dict)
#key-value
#key immutable
#value mutable
d={
    "Name":"John",
    "Age":20
}
print(d)#{"Name":"John","Age":20}
print(d["Name"])#John


#binary
#Bytes   bytesarray
#immutable
#ASCII numbers    A-65 & Z-90   a-97 & z-122
data=bytes([65,66,67])
print(data)#b'ABC'
#bytesarray
data=bytearray([65,66,67])
print(data)#bytearray(b'ABC')
data[1]=68
print(data)#bytearray(b'ADC')


#boolean
#Represent true & false
print(5>4)#True

#none
x=None
print(x)#None



#operators
#arithmetics operators     +,-,*,/,%,//,**
print(5+1)
print(4-1)
print(5*3)
print(5/2)
print(5//2)# 2
print(2**3)#2*2*2
print(5%2)


#comparision op      <,>,<=,>=,==,!=


#logical op       and ,or, not


#assignment op     +=,-=,*=,/=,%=,//=,**=
x=5
x=x+2
x+=2
print(x)#7


#bitwise op
print(5&3)#1
print(5|3)#7
print(5^3)#  same number 0 diff 1  output 6
print(~5)# change sign & add -1    output -6
print(5<<2)#   0101 add two 0 in left
print(5>>2)#   0101 add two 0 in right


#identity op
# is    is not
x=[1,2,3]
y=x
print(x is y) #True


#membership op
x=[1,2,3]
print(3 in [1,2,3])#True
print(4 not in [1,2,3])#True



#ternary op
a,b=5,3
result= a if a>b else b
print(result)#5


import math 
x=math.floor(5.9)#lower bound 
print(x) #5
y=math.ceil(5.2)#upper bound 
print(y) #6
x1=math.floor(-5.3)
print(x1)#-6
x1=math.ceil(-5.3)
print(x1)#-5

#escape sequence
print("hello123\rhello")
print("hwllo \"studemt\" ")
print("C:\\user\\name\\document")
print(r"C:\user\name\document")
#\v


#take input from user
a=input("enter a: ")
print(a)

a=input("enter a: ")
print("value of a is : "+a)

