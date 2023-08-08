# 1.using if else statement

a=[]
n=int(input("enter number of elements:"))
for i in range(n):
    k=int(input("enter the numbers\n"))
    a.append(k)
print(a)
s=int(input("enter a element to be search\n"))
if s in a:
    print(s," exists in a list")
else:
    print(s,"not exists in list")