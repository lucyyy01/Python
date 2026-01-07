# # #even 1-n
# # n=int(input("Enter a number:"))
# # count=1
# # while count<=n:
# #     if count%2==0:
# #         print(count)
# #     count+=1

# # #odd 1-n
# # n=int(input("Enter a number:"))
# # count=1
# # while count<=n:
# #     if count%2!=0:
# #         print(count)
# #     count+=1

# # #for loop
# # x="hello"
# # print(x)
# # print(x[0])
# # print(x[1])
# # print(x[2])
# # print(x[3])
# # print(x[4])

# # x="hello"
# # for i in x:
# #     print(i,end=" ")

# # r=range(1,6)
# # for i in r:
# #     print(i)

# # n=int(input("Enter number:"))
# # for i in range(1,n+1):
# #     print(i)

# # r=range(-1,-10,-3)
# # for i in r:
# #     print(i)

# # r=range(5,0,-1)
# # for i in r:
# #     print(i)
# # else:
# #     print("hello")

# #even 1-10 loop
# # for i in range(1,11):
# #     if i%2==0:
# #         print(i)

# #even 1 to n loop
# # n=int(input("Enter number:"))
# # for i in range(1,n+1):
# #     if i%2==0:
# #         print(i)

# # x="PYTHON"
# # for i in x:
# #     print(i)


# # #A-Z
# # count=65
# # while count<=90:
# #     print(chr(count),end=" ")
# #     count+=1

# #
# # n=int(input("Enter number:"))
# # count=1
# # sum=0
# # while count<=n:
# #     if count%2==0:
# #         sum+=count
# #     count+=1
# # print(sum)



# # for i in range(11):
# #     print(f"2 X {i} = {i*2}")


# # sum =0
# # for i in range(1,6):
# #     sum+=i
# # print(sum)



# # count=0
# # li=[1,2,3,5,5,6,7,8,9,10]
# # for i in li:
# #     if i%2==0:
# #         count+=1
# # print(count)


# #match case
# # no=2
# # match no:
# #     case 1:
# #         print("one")
# #     case 2:
# #         print("two")
# #     case 3:
# #         print("three")
# #     case 4:
# #         print("four")
# #     case _:
# #         print("Default case")


# # l1=[1,2,3]
# # l2=[4,5,6]
# # l3=[7,8,9]
# # no=int(input("Enter number:"))
# #  match no:
# #     case 1:
# #         print("hii")
# #     case 2:
# #         print("hii")
# #     case 3:
# #         print("hii")
# #     case 4:
# #         print("hello")
# #     case 5:
# #         print("hello")
# #     case 6:
# #         print("hello")
# #     case 7:
# #         print("byee")
# #     case 8:
# #         print("byee")
# #     case 9:
# #         print("byee")
# #     case _:
# #         print("Invaild")



# # t1=(1,2,3)
# # t2=(4,5,6)
# # t3=(7,8,9)
# # match t1:
# #     case (1,2,3):
# #         print("hi")
# #     case (4,5,6):
# #         print("hello")
# #     case (7,8,9):
# #         print("byee")

# # n=int(input("Enter number 1-9:"))
# # t1=(1,2,3)
# # t2=(4,5,6)
# # t3=(7,8,9)
# # match n:
# #     case t1:
# #         print("hi")
# #     case t2:
# #         print("hello")
# #     case t3:
# #         print("byee")




# #about string
# # x="hello student"
# # #print(x[0])
# # print(x[-7])
# # print(x[6])
# # print(x[0:6])
# # print(x[0:13])
# # print(x[:])
# # print(x[0:])
# # print(x[0:13:2])
# # print(x[::3])
# # print(x[::-1])#reverse
# # print(len(x))
# # print(x[0:len(x)])
# # print(x.lower())
# # print(x.upper())
# # print(x.title())
# # print(x.count("s"))


# # x="Hello Hiii how are you hi"
# # print(x.count("h"))
# # print(x.count("H"))
# # print(x.count("H")+x.count("h"))
# # print(x.upper().count("H"))


# # x="   Hello    "
# # print(x)
# # print(x.strip())
# # print(x.lstrip())
# # print(x.rstrip())


# # x="hii helo how are u"
# # # print(x.replace(" ",("~")))
# # print(x.replace("hii"),("helo"))
# # print(x.find("helo"))


# # x="hello" 
# # print(x.center(10,"#"))

# # #walrus operator(:=)
# # print(x:=10)

# # x=[10,20,30,40,50]
# # i =0

# # while i< (n:=len(x)):
# #     print(x[i],end=" ")
# #     i+=1

# # x=[10,20,30,40,50]
# # i=0
# # while (i:=i+1)<(n:=len(x)):
# #     print(x[i],end=" ")


# #int to binary
# # num=10
# # binary_num=bin(num)
# # print(binary_num)


# #int to oct 
# # num=10
# # octal_num=oct(num)
# # print(octal_num)


# # #int to hexa
# # num=255
# # hexa_num=hex(num)
# # print(hexa_num)


# #boolean from other data types
# print(bool(0))
# print(bool(1))
# print(bool(""))
# print(bool("hi"))
# print(bool([1,2]))
# print(bool(100))            


#more about list
# #empty list
# li=[]
# #list with integer
# li=[1,2,3,4]

# #list with mixed ele
# li=[1,2,3,"hello",True,1.5]

# #list with duplicates
# li=[1,2,2,3,4,3]

# #nested list
# nest=[[1,2],[3,4]]
# print(nest[1][0])

#append() =add at end
# fruit=["apple","banana"]
# fruit.append("grapes")
# print(fruit)

#insert() add at specific position
# fruit=["apple","banana"]
# fruit.insert(1,"grapes")
# print(fruit)

#extend() merge two list
fruit=["apple","banana","cherry"]
vegi=["carrot"]
fruit.extend(vegi)
print(fruit)


#remove()=delete by value
fruit=["apple","banana","cherry"]
fruit.remove("apple")
print(fruit)


#pop() delete by index or last element
fruit=["apple","banana","cherry"]
fruit.pop()
fruit.pop(1)
print(fruit)

#del 
fruit=["apple","banana","cherry"]
del fruit[1]
print(fruit)

#clear (remove all element)
fruit=["apple","banana","cherry"]
fruit.clear()
print(fruit)
