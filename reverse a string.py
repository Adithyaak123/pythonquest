'''a="adithya"
print(a[::-1])'''
a=str(input("enter a string:"))
revstring=" "
count=len(a)
while count>0:
      revstring=revstring+a[count-1]
      count=count-1
print("the reversed string is",revstring)