a=[2,3,1,48,9]
'''a[2:4]=[30,45]
print(a)'''
'''a[2:3]=[100,120]
print(a)'''
#append()
'''a=[12,4,6]
a.append(40)
print(a)'''
#insert()
''''a=[3,2,1]
a.insert(1,90)
print(a)'''
#extend()
''''a=[1,2,3]
b=[4,5,6]
a.extend(b)
b.extend(a)
print(a)
print(b)'''
#remove()
'''a=[1,2,3]
a.remove(2)
print(a)'''
#pop()
'''a=[1,3,5]
a.pop(1)
print(a)'''
#del()
'''a=[1,2,3]
del a
print(a)'''
#clear()
'''a=[3,5,8]
a.clear()
print(a)'''
#sort()
a=[5,3,8]
'''a.sort()
print(a)'''
'''a.sort(reverse=True)
print(a)'''
'''a=["abc","kji","ghi","Abc"]
a.sort()
print(a)'''
#reverse()
'''a=[3,5,98]
a.reverse()
print(a)'''
#+operator
'''a=[3,5,2]
b=[4,3]
print(a+b)'''
'''a=[2,5]
print(a*3)'''
#count()
'''a=[2,9,2,8]
print(a.count(2))'''
'''a=[2,5,8]
print(a.index(8))'''
'''a=[5,3,8]
print(len(a))'''
'''a=[4,2,8]
b=a.copy()
print(b)'''
#for loop
'''a=["abc","cde"]
for i in a:
 print(i)'''
 #range()
'''a=["abg","fhj","rju"]
for i in range(len(a)):
    print(a[i])'''
a=[]
n=int(input("enter a range:"))
for i in range(n):
    k=int(input("enter the numbers"))
    a.append(k)
print(a)



