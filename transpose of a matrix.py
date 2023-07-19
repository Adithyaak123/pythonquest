a=[[3,5,9],
   [8,4,9],
   [3,2,7]]
b=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        b[j][i]=a[i][j]
print(b)