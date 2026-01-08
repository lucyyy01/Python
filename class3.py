# #sort() acending
# number=[5,1,4,8,9,2]
# number.sort()
# print(number)


# #deciending
# number=[5,1,4,8,9,2]
# number.sort(reverse=True)
# print(number)


# #sort and store in another list
# number=[5,1,4,8,9,2]
# sorted_li=sorted(number)
# print(sorted_li)
# print(number)


# #list comprehension (shorter way to create list)
# #WAP to print 1 to 5 number sq
# li=[]#normal way
# for i in range(1,6):
#     li.append(i*i)
# print(li)


# #stage 1->(x) variable stage 2->loop stage3-> condition
# sq=[x**2 for x in range(1,6)]
# print(sq)



# n=[1,2,3,4,5,6,7,8,9]
# even=[i for i in n if i%2==0]
# print(even)



# fruits=["apple","banana","cherry"]
# upper_list=[i.upper() for i in fruits]
# print(upper_list)



# text="a1b2c3d4e5f6asg67"
# x=[i for i in text if i.isdigit()]
# print(x)



# sentence="python is very easy to learn"
# x=[i[0] for i in sentence.split()]
# print(x)



# x="whiteboard"
# v=["a","e","i","o","u"]
# vowel=[i for i in x if i in v]
# #vowel=[i for i in x if i in 'aeiou']
# print(vowel)


# x=[i**2 for i in range(1,11) if i%2==0]
# print(x)


# s="learn python easily"
# reversew=[i[::-1] for i in s.split()]
# print(reversew)


# x=[(i,i**2) for i in range(1,6)]
# print(x)


# sentence="this is a test sentence"
# y=[i for i in sentence.split() if len(i)>3]
# print(y)


# items=[1,"hello",3.5,5,"world"]
# x=[i for i in items if type(i)==int ]
# print(x)


# char=['A','B','C']
# x=[ord(i) for i in char]
# print(x)


# keys=['a','b','c']
# value=[1,2,3]
# my_dict={k:v for k,v in zip(keys,value)}
# print(my_dict)


# word=["madam","raccar","apple","noon"]
# palindrome=[i for i in word if i==i[::-1]]
# print(palindrome)


# #max=(iterable,key,default)
# x=[5,6,7,8,9]
# print(max(x))
# print(min(x))


# x=["Raj","Vishal","a"]
# print(max(x))
# print(min(x))


# x=["Raj","Vishal","a"]
# print(max(x,key=len))


# x=[]
# print(max(x,default="no elements"))


# x=[4,5,7,89,12,90,34]
# max=x[0]
# for i in x:
#     if(i>max):
#         max=i
# print(max)


# a=[10,20,30,40,50]
# if 50 in a:
#     print("Yes")
# else:
#     print("No")


# a=[10,20,30,40]
# b=a.copy()
# c=b
# print(a)
# print(b)
# print(c)


# a="hello"
# b=a.split()
# print(a)
# print(b)


# a=["hello","student"]
# b=','.join(a)
# print(a)
# print(b)


# #function in python
# def msg():
#     print("helloo ")

# msg()

# def sum(a,b):
#     print(a+b)
# sum(5,6)


# # def add():
# #     a=int(input("Enter a:"))
# #     b=int(input("Enter b:"))
# #     c=a+b
# #     print(c)
# # add()

# def add(a,b):
#     print(a+b)


# x=5
# y=10
# add(x,y)


# def add(a,b):
#     return a+b
# z=add(5,6)
# print(z)


# # def add(a,b):
# #     print(a+b)
# # add(int(input()),int(input()))

# #function replacement
# def add(a,b):
#     print("Sum of 2 no:",a+b)
# def add(a,b,c):
#     print("Sum of 3 no:",a+b+c)

# x=add(5,10,5)
# print(x)


# def add(a,b,c=None):
#     if c==None:
#         print("sum of 2 no:",a+b)
#     else:
#         print("sum of 3 no:",a+b+c)

# add(4,5)
# add(6,5,6)


# #keyword only argument
# def add(*,a,b,c=None):
#     if c==None:
#         print("sum of 2 no:",a+b)
#     else:
#         print("sum of 3 no:",a+b+c)


# add(a=4,b=10) #Name mandatory


# #variable argument
# def add(*a):
#     print(a)  # return in tuple form
# add(10,20,30,40)


# def add(x,y,*a):
#     print(x)
#     print(y)
#     print(a)
# add(10,20,30,40,50)


# #kW argument(variable key word argument)
# def add(**a):
#     print(a)
# add(x=5,y=10)
# #positional only argument
# def fun(x,/,y):
#     print(x,y)
# fun(5,10)
# fun(10,y=5)
# # fun(x=10,y=20) #error


# def fun(a,b,/):
#     print(a,b)
# fun(1,2)
# #fun(a=1,b=2)error
# #fun(a=5,3)error
# fun(4,5)


# def fun(a,/,b,*,c):
#     print(a,b,c)
# fun(1,2,c=3)
# #fun(1,c=2,c=3)
# fun(1,b=2,c=3)
# #fun(a=1,b=2,c=3)



# def fun(x):
#     print(x)
# def fun2():
#     a=50
#     print(a)
# a=30
# fun(a)
# print(a)
# fun2()


# def fun():
#     x=20
#     print(x)
# def fun2():
#     print(a)
# a=30
# print(a) 
# fun()
# fun2()

# #function inside function is called helper function
# def outer():
#     print("This is outer functon")
#     def inner():
#         print("this is inner function")
#     inner()
# outer()


# # def msg():
# #     print("some code")
# #     print("100 line code")
# #     print("some code")
# #     print("100 line code")
# # msg()


# def msg():
#     def x100linecode():
#         print("100 line code")
#     print("some code")
#     x100linecode()
#     print("some code")
#     x100linecode()
#         # print("100 line code")

# msg()


# #lamda function(anonymous function)

# sq=lambda x:x*x
# print(sq(5))



# #add 10 in passed value
# add=lambda x:x+10
# print(add(5))


# even=lambda x:x%2==0
# print(even(6))



# largest=lambda x,y: x if x>y else y
# print(largest(4,5))



# x=lambda no:[i*i for i in range(1,no+1)]
# print(x(5))


# #map() is iterable 
# nums=[1,2,3,4]
# sq=list(map(lambda x:x*x,nums))
# print(sq)


# #filte() iterable =return true or false =0 but false i.e skip
# nums=[1,2,3,4,5,6]
# even=list(filter(lambda x:x%2==0,nums))
# print(even)


# nums=[1,2,3]
# add1=list(map(lambda x:x+1,nums))
# print(add1)


# nums=[1,2,3,4,5,6,7,8]
# sq=list(filter(lambda x: x**2 if x%2==0 else 0,nums))
# print(sq)


# str=["10","20","30","40"]
# i=list(map(lambda x:int(x),str))
# print(i)


# li=["raj","vishal","kunal"]
# u=list(map(lambda x:x.upper(),li))
# print(u)


# li=[' hi ',' hello ']
# s=list(map(lambda x:x.strip(),li))
# print(s)



# li=[' 5 ',' raj ',' 94 ']
# s=list(map(lambda x:x.strip(),li))
# r=list(filter(lambda x:x.isdigit(),s))
# l=list(map(lambda x:int(x),filter(lambda x:x.strip().isdigit(),li)))
# print(l)
# print(s)
# print(r)


# li=[1,2,3,4,5,6,7,8,9]
# e=list(filter(lambda x: x if x%2==0 else 0,li))
# print(e)


# words=["madam","hello","level"]
# p=list(filter(lambda x:x==x[::-1],words))
# print(p)



# li=["jay","om","piyush","vikas","suraj"]
# l=list(filter(lambda x: x if len(x)>3 else 0,li))
# print(l)


# li=[-3,3,8,-4,-2,1,4]
# p=list(filter(lambda x: x>0,li))
# print(p)


# li=[5,6,7,10,11,55]
# d=list(filter(lambda x: x%5==0,li))
# print(d)


# li=["apple","banana","Vijay","aakhash","Abhi"]
# p=list(filter(lambda x:x[0] in 'aA',li))
# data=list(filter(lambda x:x.lower().startswith('a'),li))
# print(data)
# print(p)



# marks=[20,30,40,60,55,90]
# m=list(filter(lambda x: x>=40,marks))
# print(m)



# li=[{'roll':3,'age':30,'name':"jay"},{'roll':5,'age':15,'name':"om"},{'roll':6,'age':40,'name':"vijay"}]
# a=list(filter(lambda x:x['age']>18,li))
# print(a)



# n=[1,2,3,4,5]
# print(sum(number))
# print(sum(list(range(1,6))))


# def am(n):
#     for i in 



#exception handling


# try:
#     a=10
#     b=0
#     print(a/b)
# except:
#     print("error occured")

# try:    
#     x=int("hello")
#     print(x)
# except:
#     print("error occured")


# try:
#     a=10
#     b=int(input("enter number :"))
#     print(a/b)
# except:
#     print("invaild input")

    
# try:
#     a=10
#     b=2
#     print(a/b)
# except:
#     print("Error")
# else:
#     print("No error occured")


# try:
#     print("hello")
# except:
#     print("Except block")
# finally:
#     print("finally")


# age=int(input("Enter age: "))
# if age<18:
#     raise ValueError("Age must be 18")
# else:
#     print("You are eligible")



# try:
#     balance=5000
#     withdraw=int(input("Enter amount:"))
#     if withdraw>balance:
#         raise Exception("insufficent balance")
#     print("Collect cash")
# except Exception as e:
#     print(e)


#file handling
# file=open("ex.txt","w")
# file.write("Hello Student")
# file.close()


# file=open("ex.txt","r")
# x=file.read()
# print(x)
# file.close()

# file=open("ex.txt","w")
# file.write("How are u")
# file.close()

#   file=open("ex.txt","r")
#  print(file.read())
#  file.clo

#  file=open("ex.txt","r")
#  print(file.read())
# #  file.clo 

# nt(input("Enter age:"))
# if age>=18:
#     print("You can ride a bike")
# elif age=<18
#     print("You cannot ride a bike")
# else: age=18
#     print("You can ride a bike with licence hoider")

# a=int (input("Enter first angle: "))
# b=int (input("Enter second angle: "))
# c=int (input("Enter Third angle: "))
# if a>0 and b>0 and c>0 and (a+b+c==180):
#     print("Triangle is possible")
# else:
#     print("Tringle is not possible")


 