a=[[1,2],
  [5,6]]
b=[[3,4],
  [5,6]]
c=[[0,0],
  [0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j]+=a[i][k]*b[k][j]
print(c)

