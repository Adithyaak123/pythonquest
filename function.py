#function
# def one():#function definition
#     print("hello")
# one()#function call

#arguments and parameters
# def sum(a,b):#parameters
#     print(a+b)
# sum(5,4)
# sum(4,3)#arguments

# c=int(input("enter a no"))
# d=int(input("enter a no"))
# def sum(a,b):
#     print(a+b)
# sum(c,d)

#docstring
# def new():
'''this function for printong something'''
 #print("hello")
# new()
# print(new.__doc__)

#types of arguments
#default argument
# def hello(name,age=10):#age is default
#     print("welcome",name,"age is",age)
# hello("anu",20)
# hello("ponnu")

#arbitrary/variable length/*args argument
# def hello(*name):
#     print(name)
# hello("ammu","achu","anu")

#keyword argument
# def hello(b,a,c):
#     print(c,a,b)
# hello(a=5,b=3,c=4)

#arbitrary keyword argument(**kw args)
# def hlo(**data):
#     print(data)
#     print(data["a"])
# hlo(a="abc",b="efg",c="ghi")

#return statement
# def multiply(a,b):
#     return a*b
# print(multiply(4,6))

# def list(x):
#     for i in x:
#         print(i)
# a=[1,4,7,9]
# list(a)

#scope
#local scope
# def new():
#     a="good morning"
#     print(a)
# new()
#print(a),#in local scope,do not display variable on outside of the function

#global scope
# a="hello"
# def new():
#     print(a)
# new()
# print(a)#in global scope display variable on inside of the function

#pass
# def display(num):
#     if num==2:
#         pass
#     else:
#         print("number is",num)
# display(2)
    
#recursion
# def hello(n):
#     if n<=0:
#         return n
#     else:
#         return n+hello(n-1)
# print(hello(3))
    
#lambda function
# x=lambda z:z*z*z
# print(x(2))

#lambda methods
# 1.filter()
# a=[1,4,2,6,5]
# b=list(filter(lambda z:z%2==0,a))
# print(b)

#to use range() in filter()
# b=list(filter(lambda z:z%5==0,range(1,100)))
# print(b)

# 2.map()
# a=[1,2,3,4,5,6,7,8,9,10]
# b=list(map(lambda y:y**2,a))
# print(b)

#to use range() in map()
# b=list(map(lambda y:y**3,range(1,6)))
# print(b)

# 3.reduce()
# from functools import reduce
# a=[1,2,3,4,5]
# b=reduce(lambda x,y:x+y,a)
# print(b)

#to use range() in reduce()
# from functools import reduce
# b=reduce(lambda x,y:x*y,range(1,6))
# print(b)





