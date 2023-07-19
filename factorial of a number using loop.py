# a=int(input("enter a number"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)

def fact(num):
    if num<=1:
        return num
    else:
        return num*fact(num-1)
print(fact(10))