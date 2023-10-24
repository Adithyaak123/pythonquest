#types of errors
# 1.syntax error

# print(hello world)

# 2.logical error
# for i in range(1,3):
#     print(i)

# 3.runtime error(zerodivision error)
# a=8
# b=0
# print(a/b)

# 4.indentation error
#  print("welcome")

# 5.index error
# a=[3,2,7]
# print(a[5])

# 6.module not found error
# import cc

# 7.name error
# print(age)

# 8.type error
# a="abc"
# b=10
# print(a+b)

#exception handling
# 1.try
# try:
    #code to chance error 
#     age=int(input("enter a age"))
#     print(age)
# except:
    #error handling code
    # print("please input data in integer format")

# def div(x,y):
#     try:
#         a=x/y
#         print(a)
#     except:
#         print("can't divided by zero")
# b=int(input("enter an integer"))
# c=int(input("enter an integer"))
# div(b,c)

# def div(x,y):
#     try:
#         a=x/y
#         print(a)
#     except NameError:
#         print("can't divided by zero")
#     except ZeroDivisionError:
#         print("not possible")
#     except:
#         print("error....")
# div(10,4)

# finally block
#d=10
# try:
#     print(d)
# except:
#     print("not defined")
# finally:
#     print("it is always executed")

# try-except-else case
def div(x,y):
    try:
        a=x/y
        print(a)
    except:
        print("can't divided by zero")
    else:
        print("no exception",a)
    finally:
        print("always executed")
# div(10,7)
div(5,0)

# raise statement
# try:
#     age=int(input("enter a age"))
#     if age>16:
#         raise
#     else:
#         print("Age is",age)
# except:
#     print("age should be less than 16")

#assertion error
# try:
#     a=56
#     b=65
#     assert a>b,'error...'
#     print("success")
# except AssertionError as t:
#     print(t)

#user-defined exception
#example 1
# class AgeError(Exception):
#     pass
# try:
#     age=int(input("enter the age\n"))
#     if age<0:
#         raise AgeError
#     else:
#         print(age)
# except AgeError:
#     print("enter correct age")

# example 2
# class Error(Exception):
#     pass
# class ValueTooSmallError(Error):
#     pass
# class ValueTooLargeEroor(Error):
#     pass
# num=10
# while True:
#     try:
#         a=int(input("enter a number"))
#         if a<num:
#             raise ValueTooSmallError
#         elif a>num:
#             raise ValueTooLargeEroor
#         break
#     except ValueTooSmallError:
#         print("it is small")
#     except ValueTooLargeEroor:
#         print("it is large")
# print("you won it")




