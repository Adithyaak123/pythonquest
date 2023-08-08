# 1.write a python program to create a lambda function that adds 15 to a given number passed in as an argument,also create alambda function that multiplies argument x with argument y and print the result
# a=lambda z:z+15
# print(a(5))
# b=lambda x,y:x*y
# print(b(3,5))

def mul(n):
   return lambda x:x*n
result=mul(2)
print("double the number of 15=",result(15))
result=mul(3)
print("triple the number of 15=",result(15))
result=mul(4)
print("quadruple the number of 15=",result(15))
result=mul(5)
print("quintuple the number of 15=",result(15))







