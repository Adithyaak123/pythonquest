'''rows=int(input("enter number of rows:"))
for i in range(rows):
    for j in range(i+1):
         print(" * ",end='')
    print()'''


'''rows=int(input("enter no of rows:"))
for i in range(rows):
    for j in range(rows-1-i):
        print(" ",end=' ')
    for k in range(i+1):
            print("*",end=' ')
    print()'''



rows=int(input("enter the number of rows:"))
k=0
for i in range(1,rows+1):
    for space in range(1,(rows-i)+1):
        print(end=" ")
    while k!=(2*i-1):
        print("*",end="")
        k+=1
    k=0
    print()





